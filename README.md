# 🚦 Sentinel: AI-Powered Urban Traffic Management

> **A scalable, automated Traffic Violation Detection System designed to replace inefficient manual surveillance with high-precision, AI-driven enforcement for Smart City infrastructure.**

---

## 🌍 The Problem

In rapidly urbanizing smart cities, relying on human-heavy manual surveillance is inefficient, costly, and prone to oversight. During peak hours or adverse weather, critical violations—like helmetless riding, signal jumping, and illegal parking—often go undetected, directly contributing to increased accidents and urban gridlock.

**Sentinel** provides a scalable automation layer for modern infrastructure, ensuring 24/7 compliance and safer road ecosystems.

---

## ✨ Core Features

Sentinel targets the three primary pillars of modern traffic regulation:

- 🛑 **Rule Enforcement:** Real-time detection of signal jumping and wrong-lane driving using spatial heuristics.
- ⛑️ **Safety Monitoring:** Automated helmetless riding detection to enforce proactive safety gear compliance.
- 🅿️ **Urban Management:** Continuous monitoring of restricted zones to identify illegal parking and reduce congestion.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-00FFFF?style=for-the-badge&logoColor=black)

---

## 🧠 Intelligence Engine (The Model Suite)

Sentinel's backend consists of specialized deep learning modules designed for concurrent execution:

1. 🏍️ **YOLO Helmet Detection:** Scans two-wheelers to capture compliance with mandatory safety gear.
2. 🚫 **Wrong Lane Detection:** Flags vehicles driving against traffic flow or violating lane dividers.
3. 🅿️ **Illegal Parking Monitor:** Automatically flags static vehicles in restricted no-parking zones.
4. ⏱️ **Trajectory Violation Logic:** Tracks vehicle paths to accurately capture speeders and signal jumpers.
5. 🚥 **Dynamic Density Evaluation:** Analyzes intersection density to provide data for real-time signal timing optimization.

---

## ⚙️ Technical Architecture

The system follows a high-performance pipeline designed for low-latency edge or cloud inference:

**📹 Ingestion ➡️ 🔍 Pre-processing ➡️ 👀 Inference ➡️ ⚖️ Violation Logic ➡️ 🚨 Alerting**

| Stage | Description |
|---|---|
| **Ingestion** | Robust feed handling from municipal CCTV infrastructure |
| **Pre-processing** | Frame extraction, perspective correction, and noise filtering |
| **Inference** | Rapid multi-model YOLO execution to classify targets (Vehicles, Pedestrians, Helmets) |
| **Violation Logic** | Spatio-temporal matching of vehicle coordinates against defined road boundary zones |
| **Alerting** | Real-time generation of violation logs, database entry, and dashboard notifications |

---

## 📸 Demo

> Add a screenshot or GIF of detection in action here.
```
assets/demo.gif
```

---

## 🚀 Getting Started
```bash
# Clone the repository
git clone https://github.com/gaurangpatil97/sentinel

# Navigate into the project
cd sentinel

# Install dependencies
pip install -r requirements.txt

# Run on webcam
python main.py --source 0

# Run on a video file
python main.py --source path/to/video.mp4
```

---

## 🏆 Impact & Vision

Sentinel is designed as a production-ready solution for modern municipalities. By enforcing compliance with 24/7 precision, it delivers measurable outcomes for Smart City initiatives:

- 📉 **Reduces Accidents:** Active enforcement curbs reckless behavior at scale.
- 🛡️ **Improves Road Safety:** Helmet compliance and lane discipline build a fundamentally safer driving culture.
- 🏙️ **Elevates Urban Living:** Automates the hardest aspects of traffic management, freeing human officers for higher-level interventions.

---

*Built to protect, optimize, and power the smart cities of tomorrow.*
