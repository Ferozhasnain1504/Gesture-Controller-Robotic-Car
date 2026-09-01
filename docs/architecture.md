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

# 17. `docs/hardware.md`

```markdown
# Hardware Setup

## Components

- Raspberry Pi 4
- Camera
- Motor driver
- Two or four DC geared motors
- Robot chassis
- Battery
- Jumper wires

## Motor Driver

The example implementation assumes an H-bridge motor driver such as an L298N.

## GPIO Mapping

| Function | GPIO |
|---|---:|
| Left Motor IN1 | 17 |
| Left Motor IN2 | 18 |
| Right Motor IN1 | 22 |
| Right Motor IN2 | 23 |
| Left PWM | 12 |
| Right PWM | 13 |

## Important

GPIO numbers in the code use BCM numbering.

Verify the pinout for the specific Raspberry Pi and motor driver being used.

Do not power motors directly from Raspberry Pi GPIO pins.

The motor driver must provide the required motor current.

Connect Raspberry Pi ground and motor-driver logic ground appropriately.