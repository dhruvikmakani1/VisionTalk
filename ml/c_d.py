import cv2

# CAP_DSHOW is often the only way to open webcams on Windows without crashing
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Camera could not be opened with DSHOW. Trying default...")
    cap = cv2.VideoCapture(0)

print("🚀 Press 'q' to close the window if it opens.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame.")
        break

    cv2.imshow('Camera Test', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# # import os
# # import mediapipe as mp
# # import cv2
# # import matplotlib.pyplot as plt

# # DATA_DIR = './data'

# # mp_hands = mp.solutions.hands
# # mp_drawing = mp.solutions.drawing_utils
# # mp_drawing_styles = mp.solutions.drawing_styles

# # hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# # for dir_ in os.listdir(DATA_DIR):
# #     for img_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:
# #         img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
# #         img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# #         results = hands.process(img_rgb)
# #         if results.multi_hand_landmarks:
# #             for hand_landmarks in results.multi_hand_landmarks:
# #                 mp_drawing.draw_landmarks(
# #                     img_rgb, # image to draw
# #                     hand_landmarks, #model output
# #                     mp_hands.HAND_CONNECTIONS, # hand connections
# #                     mp_drawing_styles.get_default_hand_landmarks_style(),
# #                     mp_drawing_styles.get_default_hand_connections_style()
# #                 )
        
# #         plt.figure()
# #         plt.imshow(img_rgb)
# # plt.show()
# import os
# import cv2
# import mediapipe as mp
# import matplotlib.pyplot as plt

# # =====================
# # CONFIG
# # =====================
# DATA_DIR = './data'

# # Close any previous figures (IMPORTANT)
# plt.close('all')

# # =====================
# # MEDIAPIPE SETUP
# # =====================
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles

# hands = mp_hands.Hands(
#     static_image_mode=True,
#     min_detection_confidence=0.6
# )

# # =====================
# # PROCESS DATASET
# # =====================
# for dir_name in sorted(os.listdir(DATA_DIR)):
#     dir_path = os.path.join(DATA_DIR, dir_name)
#     if not os.path.isdir(dir_path):
#         continue

#     for img_name in os.listdir(dir_path)[:1]:
#         img_path = os.path.join(dir_path, img_name)

#         img = cv2.imread(img_path)
#         if img is None:
#             continue

#         # Convert BGR → RGB for MediaPipe
#         img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         results = hands.process(img_rgb)

#         # Draw landmarks ONLY if detected
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(
#                     img,
#                     hand_landmarks,
#                     mp_hands.HAND_CONNECTIONS,
#                     mp_drawing_styles.get_default_hand_landmarks_style(),
#                     mp_drawing_styles.get_default_hand_connections_style()
#                 )
#         else:
#             print(f"No hand detected in: {img_path}")

#         # Convert for matplotlib
#         img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#         # Show image (copy prevents overwrite bug)
#         plt.figure()
#         plt.imshow(img_rgb.copy())
#         plt.title(f"{dir_name} / {img_name}")
#         plt.axis('off')

# plt.show()

# # Release resources
# hands.close()
