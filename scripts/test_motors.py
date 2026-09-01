import time

from motor_driver import MotorDriver


def main():

    motor = MotorDriver()

    try:

        print("Testing FORWARD...")
        motor.forward()
        time.sleep(2)

        print("Testing STOP...")
        motor.stop()
        time.sleep(1)

        print("Testing BACKWARD...")
        motor.backward()
        time.sleep(2)

        print("Testing STOP...")
        motor.stop()
        time.sleep(1)

        print("Testing LEFT...")
        motor.left()
        time.sleep(2)

        print("Testing STOP...")
        motor.stop()
        time.sleep(1)

        print("Testing RIGHT...")
        motor.right()
        time.sleep(2)

        print("Testing STOP...")
        motor.stop()

        print("Motor test completed.")

    except KeyboardInterrupt:

        print("Emergency stop.")

    finally:

        motor.cleanup()


if __name__ == "__main__":
    main()