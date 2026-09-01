class MotorDriver:
    """
    Low-level Raspberry Pi motor driver.

    Controls two DC motors through an H-bridge
    motor driver such as L298N.
    """

    def __init__(
        self,
        left_in1=17,
        left_in2=18,
        right_in1=22,
        right_in2=23,
        left_enable=12,
        right_enable=13,
        speed=70
    ):

        try:
            import RPi.GPIO as GPIO

        except ImportError:

            raise RuntimeError(
                "RPi.GPIO is required. "
                "Run this code on a Raspberry Pi."
            )

        self.GPIO = GPIO

        # -------------------------
        # GPIO pins
        # -------------------------

        self.left_in1 = left_in1
        self.left_in2 = left_in2

        self.right_in1 = right_in1
        self.right_in2 = right_in2

        self.left_enable = left_enable
        self.right_enable = right_enable

        # -------------------------
        # GPIO configuration
        # -------------------------

        GPIO.setmode(
            GPIO.BCM
        )

        pins = [
            self.left_in1,
            self.left_in2,
            self.right_in1,
            self.right_in2,
            self.left_enable,
            self.right_enable
        ]

        for pin in pins:

            GPIO.setup(
                pin,
                GPIO.OUT,
                initial=GPIO.LOW
            )

        # -------------------------
        # PWM
        # -------------------------

        self.left_pwm = GPIO.PWM(
            self.left_enable,
            1000
        )

        self.right_pwm = GPIO.PWM(
            self.right_enable,
            1000
        )

        self.left_pwm.start(
            speed
        )

        self.right_pwm.start(
            speed
        )

        # Always start safely
        self.stop()

    # -------------------------
    # Forward
    # -------------------------

    def forward(self):

        self.GPIO.output(
            self.left_in1,
            self.GPIO.HIGH
        )

        self.GPIO.output(
            self.left_in2,
            self.GPIO.LOW
        )

        self.GPIO.output(
            self.right_in1,
            self.GPIO.HIGH
        )

        self.GPIO.output(
            self.right_in2,
            self.GPIO.LOW
        )

    # -------------------------
    # Backward
    # -------------------------

    def backward(self):

        self.GPIO.output(
            self.left_in1,
            self.GPIO.LOW
        )

        self.GPIO.output(
            self.left_in2,
            self.GPIO.HIGH
        )

        self.GPIO.output(
            self.right_in1,
            self.GPIO.LOW
        )

        self.GPIO.output(
            self.right_in2,
            self.GPIO.HIGH
        )

    # -------------------------
    # Turn left
    # -------------------------

    def left(self):

        self.GPIO.output(
            self.left_in1,
            self.GPIO.LOW
        )

        self.GPIO.output(
            self.left_in2,
            self.GPIO.HIGH
        )

        self.GPIO.output(
            self.right_in1,
            self.GPIO.HIGH
        )

        self.GPIO.output(
            self.right_in2,
            self.GPIO.LOW
        )

    # -------------------------
    # Turn right
    # -------------------------

    def right(self):

        self.GPIO.output(
            self.left_in1,
            self.GPIO.HIGH
        )

        self.GPIO.output(
            self.left_in2,
            self.GPIO.LOW
        )

        self.GPIO.output(
            self.right_in1,
            self.GPIO.LOW
        )

        self.GPIO.output(
            self.right_in2,
            self.GPIO.HIGH
        )

    # -------------------------
    # Stop
    # -------------------------

    def stop(self):

        self.GPIO.output(
            self.left_in1,
            self.GPIO.LOW
        )

        self.GPIO.output(
            self.left_in2,
            self.GPIO.LOW
        )

        self.GPIO.output(
            self.right_in1,
            self.GPIO.LOW
        )

        self.GPIO.output(
            self.right_in2,
            self.GPIO.LOW
        )

    # -------------------------
    # Cleanup
    # -------------------------

    def cleanup(self):

        self.stop()

        self.left_pwm.stop()
        self.right_pwm.stop()

        self.GPIO.cleanup()