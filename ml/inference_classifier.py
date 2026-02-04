# import socketio
# import time

# # ------------------ Socket.IO ------------------
# sio = socketio.Client()
# sio.connect("http://localhost:5000")

# print("Inference started (NO CAMERA MODE)")

# """
# IMPORTANT:
# - We do NOT open the webcam here.
# - Browser (WebRTC) already uses the camera.
# - This avoids OS-level camera conflicts.
# - This script only sends captions.
# """

# # Demo captions (replace later with real ML output if needed)
# demo_signs = ["1", "2", "3", "4", "5"]

# i = 0
# while True:
#     caption = demo_signs[i % len(demo_signs)]
#     sio.emit("caption", caption)
#     print(f"Sent caption: {caption}")
#     i += 1
#     time.sleep(1)

import pickle
import cv2
import mediapipe as mp
import numpy as np
import time

# ------------------ Load model ------------------
try:
    model_dict = pickle.load(open('./model.p', 'rb'))
    model = model_dict['model']
    print("✅ Model loaded")
except Exception as e:
    print(f"❌ Load error: {e}")
    exit()

# ------------------ Camera setup ------------------
# Use the backend that worked in your test
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 

# ------------------ MediaPipe setup ------------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
# Set static_image_mode to False for faster video tracking
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

labels_dict = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E',
    'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J',
    'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O',
    'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
    'Z': 'Z'
}


print("🚀 System Running... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        # We only process the first hand detected
        hand_landmarks = results.multi_hand_landmarks[0]
        
        # Draw landmarks immediately so you see it's working
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        data_aux = []
        x_ = []
        y_ = []

        for lm in hand_landmarks.landmark:
            x_.append(lm.x)
            y_.append(lm.y)

        for lm in hand_landmarks.landmark:
            data_aux.append(lm.x - min(x_))
            data_aux.append(lm.y - min(y_))

        # --- CRITICAL SAFETY CHECK ---
        # Your model likely expects 42 features (21 landmarks * x and y)
        if len(data_aux) == 42:
            try:
                prediction = model.predict([np.asarray(data_aux)])
                predicted_character = labels_dict.get(int(prediction[0]), "Unknown")
                
                # Draw prediction text
                cv2.putText(frame, predicted_character, (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            except Exception as e:
                # If prediction fails, print error but DON'T close the window
                print(f"Prediction error: {e}")
        else:
            # If MediaPipe detects more or fewer points, don't try to predict
            print(f"⚠️ Wrong data shape: {len(data_aux)}. Expected 42.")

    cv2.imshow('Hand Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
