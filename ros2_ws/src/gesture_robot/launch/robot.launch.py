from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    # -----------------------------
    # Gesture Detection Node
    # -----------------------------
    gesture_node = Node(
        package="gesture_robot",
        executable="gesture_node",
        name="gesture_node",
        output="screen"
    )

    # -----------------------------
    # Motor Control Node
    # -----------------------------
    motor_node = Node(
        package="gesture_robot",
        executable="motor_node",
        name="motor_node",
        output="screen"
    )

    # -----------------------------
    # Launch both nodes
    # -----------------------------
    return LaunchDescription([
        gesture_node,
        motor_node
    ])