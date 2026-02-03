import os
import cv2

DATA_DIR = './data'
os.makedirs(DATA_DIR, exist_ok=True)

number_of_classes = 1
dataset_size = 100

# Try different camera index (0, 1, 2, etc.)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera. Please check camera index.")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    os.makedirs(class_dir, exist_ok=True)

    print(f'Collecting data for class {j}')
    print('Press "q" to start...')

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.putText(frame, 'Ready? Press "Q" to start', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.imshow('frame', frame)
        cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)
        counter += 1

        print(f'Saved {counter}/{dataset_size}', end='\r')

cap.release()
cv2.destroyAllWindows()
