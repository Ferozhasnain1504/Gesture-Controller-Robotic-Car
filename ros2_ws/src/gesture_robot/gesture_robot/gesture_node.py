import cv2
import rclpy

from rclpy.node import Node
from std_msgs.msg import String

from .gesture_detector import GestureDetector


class GestureNode(Node):
    """
    ROS 2 node responsible for:

    Camera
        ↓
    MediaPipe
        ↓
    Gesture Detection
        ↓
    ROS 2 Command Publisher
    """

    def __init__(self):
        super().__init__("gesture_node")

        # -------------------------
        # ROS Publisher
        # -------------------------

        self.publisher = self.create_publisher(
            String,
            "/robot/cmd",
            10
        )

        # -------------------------
        # Gesture Detector
        # -------------------------

        self.detector = GestureDetector(
            detection_confidence=0.6,
            tracking_confidence=0.6
        )

        # -------------------------
        # Camera
        # -------------------------

        self.camera = cv2.VideoCapture(0)

        self.camera.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            640
        )

        self.camera.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            480
        )

        if not self.camera.isOpened():

            self.get_logger().error(
                "Could not open camera."
            )

        # -------------------------
        # Timer
        # -------------------------

        # 20 FPS approximately
        self.timer = self.create_timer(
            0.05,
            self.process_frame
        )

        self.last_gesture = None
        self.last_command = None

        self.get_logger().info(
            "Gesture Node started."
        )

    def process_frame(self):

        # Read camera frame
        success, frame = self.camera.read()

        if not success:

            self.get_logger().warning(
                "Failed to capture camera frame."
            )

            return

        # Flip image so it behaves like a mirror
        frame = cv2.flip(
            frame,
            1
        )

        # MediaPipe processing
        results = self.detector.process(
            frame
        )

        # Detect gesture
        gesture = self.detector.detect_gesture(
            results
        )

        # Map gesture to robot command
        command = self.gesture_to_command(
            gesture
        )

        # Publish command
        message = String()
        message.data = command

        self.publisher.publish(
            message
        )

        # Log only when command changes
        if command != self.last_command:

            self.get_logger().info(
                f"Gesture: {gesture} | "
                f"Command: {command}"
            )

            self.last_command = command

        # Draw landmarks
        frame = self.detector.draw_landmarks(
            frame,
            results
        )

        # Display gesture
        cv2.putText(
            frame,
            f"Gesture: {gesture}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        # Display command
        cv2.putText(
            frame,
            f"Command: {command}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        cv2.imshow(
            "Gesture Controlled Robot",
            frame
        )

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):

            self.get_logger().info(
                "Stopping gesture node..."
            )

            rclpy.shutdown()

    @staticmethod
    def gesture_to_command(gesture):

        mapping = {

            "FIST": "FORWARD",

            "THUMB_UP": "BACKWARD",

            "POINT_LEFT": "LEFT",

            "POINT_RIGHT": "RIGHT",

            "OPEN_PALM": "STOP",

            "UNKNOWN": "STOP"
        }

        return mapping.get(
            gesture,
            "STOP"
        )

    def cleanup(self):

        self.camera.release()

        cv2.destroyAllWindows()

        self.detector.close()

    def destroy_node(self):

        self.cleanup()

        super().destroy_node()


def main(args=None):

    rclpy.init(
        args=args
    )

    node = GestureNode()

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