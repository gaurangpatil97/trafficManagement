import cv2
import numpy as np
from ultralytics import YOLO
from collections import deque

# ── 1. MANUAL CALIBRATION SETUP ─────────────────────────────────────────────
VIDEO_PATH = r"E:\trafficManagement\backend\models\yoloSpeedDetection\speed1.mp4"

# UK HIGHWAY STANDARDS: 1 line (2m) + 1 gap (7m) = 9 meters total per cycle.
# Count the cycles in your clicked area and update this number!
REAL_HEIGHT = 90  # Default estimate for a 10-cycle stretch
REAL_WIDTH = 12   # Standard 3-lane width (~3.6m per lane)

clicked_points = []

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append([x, y])
        cv2.circle(calib_frame, (x, y), 5, (0, 0, 255), -1)
        if len(clicked_points) > 1:
            cv2.line(calib_frame, tuple(clicked_points[-2]), tuple(clicked_points[-1]), (0, 255, 0), 2)
        cv2.imshow("CALIBRATION", calib_frame)

# Start Calibration
cap = cv2.VideoCapture(VIDEO_PATH)
ret, calib_frame = cap.read()
cv2.imshow("CALIBRATION", calib_frame)
cv2.setMouseCallback("CALIBRATION", click_event)
print("📍 Click 4 points: Top-Left, Top-Right, Bottom-Right, Bottom-Left. Press any key to start.")
cv2.waitKey(0)
cv2.destroyAllWindows()

if len(clicked_points) != 4:
    print("❌ Error: 4 points required."); exit()

# ── 2. PERSPECTIVE MATH ──────────────────────────────────────────────────────
SOURCE_POLY = np.array(clicked_points, dtype=np.float32)
TARGET_POLY = np.array([[0, 0], [REAL_WIDTH, 0], [REAL_WIDTH, REAL_HEIGHT], [0, REAL_HEIGHT]], dtype=np.float32)
M = cv2.getPerspectiveTransform(SOURCE_POLY, TARGET_POLY)

# ── 3. DETECTION & TRACKING SETUP ────────────────────────────────────────────
model = YOLO("yolov8n.pt")
fps = cap.get(cv2.CAP_PROP_FPS) or 30
track_history = {}
speed_history = {}
SMOOTHING_FACTOR = 0.10  # Lower = less jitter, but slower response

def get_speed(history, fps):
    if len(history) < fps / 2: return 0
    # Map pixels to meters
    pts = np.array([history[0], history[-1]], dtype=np.float32).reshape(-1, 1, 2)
    transformed = cv2.perspectiveTransform(pts, M).reshape(-1, 2)
    distance = np.linalg.norm(transformed[1] - transformed[0])
    return (distance / (len(history) / fps)) * 3.6

# ── 4. MAIN PROCESSING LOOP ──────────────────────────────────────────────────
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    results = model.track(frame, persist=True, verbose=False, classes=[2, 3, 5, 7])

    if results[0].boxes.id is not None:
        ids = results[0].boxes.id.cpu().numpy()
        boxes = results[0].boxes.xyxy.cpu().numpy()
        
        for tid, box in zip(ids, boxes):
            x1, y1, x2, y2 = map(int, box)
            foot_pos = [(x1 + x2) / 2, y2] 
            
            # Check if vehicle is inside the measurement zone
            is_inside = cv2.pointPolygonTest(SOURCE_POLY, (foot_pos[0], foot_pos[1]), False) >= 0

            if is_inside:
                if tid not in track_history:
                    track_history[tid] = deque(maxlen=int(fps))
                    speed_history[tid] = 0
                track_history[tid].append(foot_pos)

                raw_v = get_speed(track_history[tid], fps)
                
                # --- NOISE FILTER ---
                # 1. Ignore speeds below 7km/h (Pixel Jitter)
                # 2. Apply Exponential Moving Average (EMA)
                if raw_v > 7:
                    speed_history[tid] = (SMOOTHING_FACTOR * raw_v) + ((1 - SMOOTHING_FACTOR) * speed_history[tid])
                else:
                    speed_history[tid] = 0

                display_v = int(speed_history[tid])
                color = (0, 255, 0) # Green for active detection
                label = f"ID:{int(tid)} {display_v} km/h"
            else:
                color = (0, 165, 255) # Orange for "Waiting/Outside"
                label = f"ID:{int(tid)} Tracking..."

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Visual overlays
    cv2.polylines(frame, [SOURCE_POLY.astype(np.int32)], True, (255, 255, 255), 2)
    cv2.imshow("Neural Nexus - Calibrated Speed Enforcement", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()