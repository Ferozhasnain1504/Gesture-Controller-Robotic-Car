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