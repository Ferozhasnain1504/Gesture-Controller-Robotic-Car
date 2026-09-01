from setuptools import setup
import os
from glob import glob


package_name = "gesture_robot"


setup(
    name=package_name,
    version="1.0.0",

    packages=[
        package_name
    ],

    data_files=[
        (
            "share/ament_index/resource_index/packages",
            [
                "resource/" + package_name
            ]
        ),

        (
            "share/" + package_name,
            ["package.xml"]
        ),

        (
            os.path.join(
                "share",
                package_name,
                "launch"
            ),
            glob("launch/*.py")
        ),
    ],

    install_requires=[
        "setuptools"
    ],

    zip_safe=True,

    description=(
        "Gesture controlled robotic car "
        "using MediaPipe and ROS 2."
    ),

    license="MIT",

    entry_points={
        "console_scripts": [
            "gesture_node = "
            "gesture_robot.gesture_node:main",

            "motor_node = "
            "gesture_robot.motor_node:main",
        ],
    },
)