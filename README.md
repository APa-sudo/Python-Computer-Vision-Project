# Real-Time Hand Gesture Recognition using OpenCV and MediaPipe

## Overview

This project implements a real-time hand gesture recognition system using **Python**, **OpenCV**, and **MediaPipe**. The application detects hand landmarks from a live webcam feed and classifies predefined gestures based on the relative positions of finger joints.

Currently, the system can recognize:

* Open Palm
* Closed Fist
* Pinch Gesture (Thumb and Index Finger)

To improve robustness, gesture stabilization is implemented using a frame-based confirmation mechanism, reducing false detections caused by tracking noise and temporary landmark fluctuations.

---

## Features

* Real-time webcam-based hand tracking
* Hand landmark detection using MediaPipe
* Gesture classification using geometric landmark relationships
* Stable gesture recognition through temporal filtering
* Visual hand skeleton rendering
* Pinch distance measurement and visualization
* HD display output with optimized internal processing resolution

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

---

## How It Works

### Hand Detection

MediaPipe Hands is used to detect and track 21 hand landmarks in real time.

### Gesture Recognition

Gestures are recognized by comparing the positions of finger landmarks.

#### Palm Detection

A palm is detected when all fingertips are positioned above their corresponding finger joints.

#### Fist Detection

A fist is detected when all fingertips are folded below their corresponding finger joints.

#### Pinch Detection

A pinch is detected by measuring the Euclidean distance between the thumb tip and index fingertip.

### Gesture Stabilization

Raw detections often fluctuate due to:

* Small hand movements
* Camera noise
* Landmark estimation inaccuracies

To improve reliability, a gesture must be detected consistently for multiple consecutive frames before becoming the active recognized gesture.

---

## Project Structure

```text
Python-Computer-Vision-Project/
│
├── src/
│   └── gesture_recognition.py
│
├── experiments/
│   ├── opencv_experiments/
│   └── mediapipe_experiments/
│
├── assets/
│   ├── screenshots/
│   └── demo_gifs/
│
├── README.md
└── requirements.txt
```

---


## Current Gestures

| Gesture | Detection Logic                                     |
| ------- | --------------------------------------------------- |
| Palm    | All fingers extended                                |
| Fist    | All fingers folded                                  |
| Pinch   | Thumb and index fingertip within threshold distance |

---

## Future Improvements

* Gesture-controlled Windows actions
* Volume and media control
* Mouse cursor control
* Multi-hand support

---

## Skills Demonstrated

* Computer Vision
* Real-Time Image Processing
* Geometric Reasoning
* State Machine Design
* Human-Computer Interaction
* Debugging and System Stabilization
* Software Development with Python

---

## Lessons Learned

This project provided practical experience in:

* Building real-time computer vision pipelines
* Working with landmark-based geometric analysis
* Handling noisy sensor data
* Designing stable gesture recognition systems
* Optimizing performance for interactive applications

---

## Author

**Akshat Pathak**
Robotics Engineering Student
Technische Hochschule Würzburg-Schweinfurt (THWS)
