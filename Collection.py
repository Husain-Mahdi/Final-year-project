import os
import cv2

DATA_DIR = './Signs'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 26
dataset_size = 100
cap = cv2.VideoCapture(0)

for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))
    print('Collecting data for class {}'.format(j))

    done = False
    image_count = 0
    while image_count < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            done = True
            break
        elif key == ord('c'):
            image_count += 1
            cv2.imwrite(os.path.join(DATA_DIR, str(j), 'image_{}.png'.format(image_count)), frame)
            print('Captured image {} for class {}'.format(image_count, j))

    if done:
        break

cap.release()
cv2.destroyAllWindows()
