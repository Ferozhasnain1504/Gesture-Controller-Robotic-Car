# System Architecture

## Overview

The robotic car follows a perception → decision → communication → actuation architecture.

```text
Camera
   ↓
OpenCV
   ↓
MediaPipe
   ↓
Gesture Classification
   ↓
Gesture Mapping
   ↓
ROS 2 Topic
   ↓
Motor Controller Node
   ↓
GPIO
   ↓
Motor Driver
   ↓
DC Motors
```
## Perception Layer

The camera continuously captures frames.

OpenCV provides the image frames to MediaPipe.

MediaPipe identifies hand landmarks.

The gesture detector analyzes the landmarks and identifies a gesture.

Decision Layer

The gesture is converted into a standardized robot command.

Examples:
```text
FIST → FORWARD
THUMB_UP → BACKWARD
POINT_LEFT → LEFT
POINT_RIGHT → RIGHT
OPEN_PALM → STOP
```

## Communication Layer

ROS 2 provides communication between the gesture-processing and motor-control modules.

The gesture node publishes commands to:

```
/robot/cmd
```

The motor node subscribes to this topic.

## Actuation Layer

The motor controller receives commands and controls Raspberry Pi GPIO pins.

The GPIO signals are connected to the motor driver's input pins.

The motor driver supplies the required current to the DC motors.

### Design Benefits
* Modular architecture
* Independent perception and actuation
* Easy debugging
* Hardware abstraction
* ROS-based communication
* Expandable to additional sensors

---
