import cv2
import mediapipe as mp


class GestureDetector:
    """
    Detects hand landmarks using MediaPipe
    and classifies basic hand gestures.
    """

    def __init__(
        self,
        detection_confidence=0.6,
        tracking_confidence=0.6
    ):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

    def process(self, frame):
        """Process a camera frame using MediaPipe."""

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        return self.hands.process(rgb_frame)

    def draw_landmarks(self, frame, results):
        """Draw detected hand landmarks on the frame."""

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return frame

    def detect_gesture(self, results):
        """
        Classify the detected hand into a basic gesture.

        Returns:
            FIST
            OPEN_PALM
            THUMB_UP
            POINT_LEFT
            POINT_RIGHT
            UNKNOWN
        """

        if not results.multi_hand_landmarks:
            return "UNKNOWN"

        landmarks = results.multi_hand_landmarks[0].landmark

        # Landmark indices:
        # Wrist = 0
        # Thumb tip = 4
        # Index tip = 8
        # Middle tip = 12
        # Ring tip = 16
        # Pinky tip = 20

        fingers_up = 0

        # Index
        if landmarks[8].y < landmarks[6].y:
            fingers_up += 1

        # Middle
        if landmarks[12].y < landmarks[10].y:
            fingers_up += 1

        # Ring
        if landmarks[16].y < landmarks[14].y:
            fingers_up += 1

        # Pinky
        if landmarks[20].y < landmarks[18].y:
            fingers_up += 1

        # -------------------------
        # OPEN PALM
        # -------------------------

        if fingers_up >= 4:
            return "OPEN_PALM"

        # -------------------------
        # FIST
        # -------------------------

        if fingers_up == 0:
            return "FIST"

        # -------------------------
        # THUMB UP
        # -------------------------

        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]

        if (
            thumb_tip.y < thumb_ip.y
            and fingers_up <= 1
        ):
            return "THUMB_UP"

        # -------------------------
        # POINTING
        # -------------------------

        if fingers_up == 1:

            index_tip = landmarks[8]
            index_pip = landmarks[6]

            # Finger pointing upward
            if index_tip.y < index_pip.y:

                # Determine horizontal direction
                wrist = landmarks[0]

                if index_tip.x < wrist.x:
                    return "POINT_LEFT"

                return "POINT_RIGHT"

        return "UNKNOWN"

    def close(self):
        """Release MediaPipe resources."""

        self.hands.close()