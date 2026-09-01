# Gesture Recognition

## Supported Gestures

```text
* FIST : FORWARD
* THUMB_UP : BACKWARD
* POINT_LEFT : LEFT
* POINT_RIGHT : RIGHT
* OPEN_PALM : STOP 
```

## Gesture Pipeline

Camera Frame
     ↓
RGB Conversion
     ↓
MediaPipe Hand Detection
     ↓
Hand Landmarks
     ↓
Gesture Classification
     ↓
Robot Command

## Improving Recognition

The current classifier is intentionally lightweight.

For improved robustness, the project can be extended using:

* Landmark normalization
* Finger-angle calculations
* Temporal smoothing
* Gesture confidence thresholds
* Machine-learning based gesture classifier
* Multi-frame voting


---
