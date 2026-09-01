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

# 19. `setup.sh`

```bash
#!/bin/bash

set -e

echo "=================================="
echo "Gesture Robot Setup"
echo "=================================="

echo "[1/4] Installing Python dependencies..."

python3 -m pip install --upgrade pip

python3 -m pip install -r requirements.txt


echo "[2/4] Installing ROS dependencies..."

cd ros2_ws

rosdep install \
    --from-paths src \
    --ignore-src \
    -r \
    -y


echo "[3/4] Building ROS workspace..."

source /opt/ros/humble/setup.bash

colcon build


echo "[4/4] Setup complete."

echo ""
echo "Run:"
echo ""
echo "source install/setup.bash"
echo ""
echo "Then:"
echo ""
echo "ros2 launch gesture_robot robot.launch.py"