from flask import Flask, render_template, Response, jsonify
import cv2
from gesture_recognition import GestureRecognizer
import threading

app = Flask(__name__)
cap = cv2.VideoCapture(0)
recognizer = GestureRecognizer()

# Variable global para almacenar el último conteo
latest_hand_data = []

def capture_loop():
    global latest_hand_data
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        frame, hand_data = recognizer.recognize(frame)
        latest_hand_data = hand_data

        # Mostrar en el frame el total
        total = sum([h['fingers_up'] for h in hand_data])
        cv2.putText(frame, f'Total dedos: {total}', (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(capture_loop(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/finger_count')
def finger_count():
    return jsonify(latest_hand_data)

if __name__ == '__main__':
    threading.Thread(target=lambda: app.run(debug=True, use_reloader=False)).start()
