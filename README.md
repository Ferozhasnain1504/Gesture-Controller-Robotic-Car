# Gesture Controlled Robotic Car

A real-time gesture-controlled robotic car built using **Python, MediaPipe, Raspberry Pi 4, GPIO and ROS 2**.

The system uses a camera to detect hand gestures using MediaPipe, converts the detected gestures into motion commands, and communicates those commands through ROS 2 to a motor-control node running on the Raspberry Pi.

## 🚗 Features

* Real-time hand gesture detection
* MediaPipe hand landmark tracking
* Gesture-to-motion command mapping
* Raspberry Pi 4 GPIO motor control
* ROS 2 based inter-module communication
* On-device processing
* Emergency stop gesture
* Configurable GPIO pins
* Modular perception and actuation architecture

## 🏗️ System Architecture

```text
                Camera
                   │
                   ▼
        ┌────────────────────┐
        │   MediaPipe        │
        │ Hand Detection     │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Gesture Detector   │
        │ Python Module      │
        └─────────┬──────────┘
                  │
             Gesture Command
                  │
                  ▼
        ┌────────────────────┐
        │     ROS 2          │
        │  Communication     │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │   Motor Control    │
        │      Node          │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Raspberry Pi GPIO   │
        └─────────┬──────────┘
                  │
                  ▼
             Motor Driver
                  │
                  ▼
              DC Motors
```

## ✋ Gesture Controls

| Gesture     | Command    | Robot Action  |
| ----------- | ---------- | ------------- |
| Open Palm   | `STOP`     | Stop          |
| Fist        | `FORWARD`  | Move forward  |
| Thumb Up    | `BACKWARD` | Move backward |
| Point Right | `RIGHT`    | Turn right    |
| Point Left  | `LEFT`     | Turn left     |

The gesture mapping can be modified in:

```text
ros2_ws/src/gesture_robot/gesture_robot/gesture_mapping.py
```

## 🧰 Hardware

### Required Components

* Raspberry Pi 4
* Raspberry Pi compatible camera / USB webcam
* L298N or equivalent motor driver
* 2/4 DC geared motors
* Robot chassis
* Battery pack
* Jumper wires

### Example GPIO Configuration

| Motor Driver | Raspberry Pi |
| ------------ | ------------ |
| IN1          | GPIO 17      |
| IN2          | GPIO 18      |
| IN3          | GPIO 22      |
| IN4          | GPIO 23      |
| ENA          | GPIO 12      |
| ENB          | GPIO 13      |

> GPIO numbers are configurable. Verify your actual wiring before powering the motors.

## 💻 Software Requirements

* Ubuntu 22.04 / Raspberry Pi OS compatible setup
* Python 3
* ROS 2 Humble or compatible ROS 2 distribution
* OpenCV
* MediaPipe
* NumPy
* GPIO library

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/gesture-controlled-robotic-car.git

cd gesture-controlled-robotic-car
```

Install Python dependencies:

```bash
pip3 install -r requirements.txt
```

Install ROS dependencies:

```bash
cd ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```

Build the ROS workspace:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

## ▶️ Running the Robot

Start the complete system:

```bash
ros2 launch gesture_robot robot.launch.py
```

The system will start:

1. Camera input
2. MediaPipe gesture detection
3. ROS 2 gesture publisher
4. ROS 2 motor controller
5. Raspberry Pi GPIO motor control

## 🔍 ROS 2 Communication

The gesture detector publishes commands to:

```text
/robot/cmd
```

Example:

```bash
ros2 topic echo /robot/cmd
```

Possible messages:

```text
FORWARD
BACKWARD
LEFT
RIGHT
STOP
```

## 🧪 Testing Motors

Before running the vision system, test the motor driver:

```bash
python3 scripts/test_motors.py
```

**Keep the robot elevated during initial motor testing.**

## 🛑 Safety

Always test the motor-control system with the wheels off the ground initially.

Use an emergency stop command whenever possible:

```bash
ros2 topic pub --once /robot/cmd std_msgs/msg/String "{data: 'STOP'}"
```

Disconnect the battery if the motors behave unexpectedly.

## 📂 Project Structure

```text
gesture-controlled-robotic-car/
│
├── config/
├── docs/
├── scripts/
├── requirements.txt
├── setup.sh
│
└── ros2_ws/
    └── src/
        └── gesture_robot/
            ├── package.xml
            ├── setup.py
            ├── setup.cfg
            ├── resource/
            ├── gesture_robot/
            │   ├── gesture_detector.py
            │   ├── gesture_node.py
            │   ├── motor_driver.py
            │   ├── motor_node.py
            │   └── gesture_mapping.py
            └── launch/
                └── robot.launch.py
```

## 🔮 Future Improvements

* Add obstacle detection
* Add ultrasonic sensor integration
* Add PID-based motor control
* Add motor speed control
* Add gesture confidence filtering
* Add autonomous/manual control switching
* Add web-based robot dashboard
* Add battery monitoring
* Add ROS 2 diagnostics
* Add recording and replay of gesture commands

## 👨‍💻 Author

**Your Name**

Electronics & Communication Engineering

---

## License

This project is licensed under the MIT License.
