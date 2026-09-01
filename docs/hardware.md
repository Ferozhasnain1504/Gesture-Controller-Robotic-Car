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