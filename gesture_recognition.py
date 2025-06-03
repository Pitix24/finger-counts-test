import cv2
import mediapipe as mp

class GestureRecognizer:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]

    def recognize(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        hand_data = []
        if results.multi_hand_landmarks and results.multi_handedness:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                self.mp_draw.draw_landmarks(
                    frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

                hand_label = results.multi_handedness[idx].classification[0].label  # Left or Right
                landmarks = hand_landmarks.landmark
                fingers = []

                # Pulgar
                if hand_label == "Right":
                    fingers.append(landmarks[self.tip_ids[0]].x < landmarks[self.tip_ids[0] - 1].x)
                else:
                    fingers.append(landmarks[self.tip_ids[0]].x > landmarks[self.tip_ids[0] - 1].x)

                # Otros dedos
                for id in range(1, 5):
                    fingers.append(landmarks[self.tip_ids[id]].y < landmarks[self.tip_ids[id] - 2].y)

                hand_data.append({
                    'label': hand_label,
                    'fingers_up': sum(fingers)
                })

        return frame, hand_data
