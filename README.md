# 🚦 Sentinel

> **An Automated Traffic Violation Detection System designed to eliminate the inefficiencies of human-heavy surveillance, ensuring smarter, safer, and self-regulating urban mobility.**

---

## 🌍 The Problem

In rapidly urbanizing smart cities, relying on manual, human-heavy surveillance for traffic management is proving highly inefficient, costly, and error-prone. Countless violations go undetected during peak hours or adverse conditions, leading to increased accidents, fatal injuries, and widespread traffic congestion. 

**Sentinel** was built to solve this by bringing a scalable, AI-driven automation layer directly to modern urban infrastructure.

---

## ✨ Core Features

Our solution targets three critical pillars of modern traffic management:

- 🛑 **Rule Enforcement:** Automated, split-second detection of signal jumping and wrong-lane driving.
- ⛑️ **Safety Monitoring:** Real-time helmetless riding detection to effortlessly enforce proactive gear usage.
- 🅿️ **Urban Management:** Continuous identification of illegal parking to drastically reduce gridlocks and keep city arteries clear.

---

## 🧠 Backend Intelligence (The Models)

The true brain of Sentinel resides in its advanced deep learning backend. Our architecture relies on a suite of **five** specialized computer vision models working concurrently to monitor and alert on diverse road scenarios. 

*(Note: These models represent our comprehensive roadmap. While parts are under active development, the full model suite will be deployed soon!)*

1. 🏍️ **YOLO Helmet Detection** (`yolohelmetDetection`): Scans two-wheelers in real-time to capture compliance for mandatory safety helmets.
2. 🚫 **Wrong Lane Driving Detection** (`wrongLaneDrivingDetection`): Flags vehicles driving against the flow of traffic or violating strict lane dividers.
3. 🅿️ **Illegal Parking Detection** (`illegalParkingDetection`): Constantly monitors no-parking zones and automatically flags static, illegally parked vehicles.
4. ⏱️ **YOLO Speed / Signal Violation Detection** (`yoloSpeedDetection`): Accurately tracks vehicle trajectories to capture speeders and signal jumpers.
5. 🚥 **Dynamic Traffic Signal Adjustment** (`dynamicTrafficSignalTime`): Evaluates intersection density dynamically, adjusting signal timings in real-time to optimize flow.

---

## ⚙️ Technical Architecture

Sentinel relies on a highly optimized, state-of-the-art pipeline designed for ultra-low latency edge or cloud inference:

**📹 Live Video Stream ➡️ 🔍 Pre-processing ➡️ 👀 YOLO Object Detection ➡️ ⚖️ Violation Logic ➡️ 🚨 Alert System**

1. **Live Video Stream:** Continuous, robust feeds ingested directly from municipal CCTV cameras.
2. **Pre-processing:** Frame extraction, perspective correction, and noise reduction.
3. **YOLO Object Detection:** Rapid multi-model inference to classify targets like cars, bikes, pedestrians, and helmets.
4. **Violation Logic:** Spatio-temporal heuristics matching vehicle coordinates against defined road zones (e.g., solid lines, zebra crossings).
5. **Alert System:** Immediate generation of actionable violations, seamless database logging, and real-time dashboard notifications.

---

## 🏆 Impact & Vision

Sentinel is structurally designed as a **production-ready, enterprise-grade solution for modern municipalities**. 

By capturing non-compliance with 24/7 unblinking precision, Sentinel achieves unprecedented outcomes for Smart City initiatives:
- 📉 **Reduces Accidents:** Active enforcement of rules dramatically curbs reckless behavior.
- 🛡️ **Improves Road Safety:** Ensuring helmet compliance and lane discipline builds a fundamentally safer driving culture.
- 🏙️ **Elevates Urban Living:** Automates the hardest aspects of municipal traffic management, freeing human enforcement officers to handle higher-level tasks and interventions.

<br>

**Built to protect, optimize, and power the smart cities of tomorrow.**
