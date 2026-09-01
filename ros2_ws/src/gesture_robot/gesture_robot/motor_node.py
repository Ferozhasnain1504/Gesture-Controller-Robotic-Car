import rclpy

from rclpy.node import Node
from std_msgs.msg import String

from .motor_driver import MotorDriver


class MotorNode(Node):
    """
    ROS 2 node responsible for receiving
    movement commands and controlling the motors.
    """

    def __init__(self):

        super().__init__(
            "motor_node"
        )

        # -------------------------
        # Motor driver
        # -------------------------

        self.motor = MotorDriver()

        # -------------------------
        # ROS subscriber
        # -------------------------

        self.subscription = self.create_subscription(
            String,
            "/robot/cmd",
            self.command_callback,
            10
        )

        self.get_logger().info(
            "Motor Node started."
        )

        self.get_logger().info(
            "Listening on /robot/cmd"
        )

    def command_callback(self, message):

        command = message.data.upper().strip()

        self.get_logger().info(
            f"Received command: {command}"
        )

        if command == "FORWARD":

            self.motor.forward()

        elif command == "BACKWARD":

            self.motor.backward()

        elif command == "LEFT":

            self.motor.left()

        elif command == "RIGHT":

            self.motor.right()

        elif command == "STOP":

            self.motor.stop()

        else:

            self.get_logger().warning(
                f"Unknown command: {command}"
            )

            # Safety fallback
            self.motor.stop()

    def destroy_node(self):

        # Always stop motors before exiting
        self.motor.stop()

        self.motor.cleanup()

        super().destroy_node()


def main(args=None):

    rclpy.init(
        args=args
    )

    node = MotorNode()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:

        pass

    finally:

        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()