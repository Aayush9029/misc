import cv2  # import opencv
import tensorflow.keras as keras
import numpy as np
from pyautogui import press
import time
import os
handUp = False

counter = 0


np.set_printoptions(suppress=True)

webcam = cv2.VideoCapture(0)
model = keras.models.load_model('keras_model.h5')
data_for_model = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def load_labels(path):
    f = open(path, 'r')
    lines = f.readlines()
    labels = []
    for line in lines:
        labels.append(line.split(' ')[1].strip('\n'))
    return labels


label_path = 'labels.txt'
print("loading model to memory")
labels = load_labels(label_path)
print("done")


def image_resize(image, height, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    r = height / float(h)
    dim = (int(w * r), height)
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


def cropTo(img):
    _, width = img.shape[:2]
    sideCrop = (width - 224) // 2
    return img[:, sideCrop:(width - sideCrop)]


while True:
    ret, img = webcam.read()
    if ret:
        # same as the cropping process in TM2
        img = image_resize(img, height=224)
        img = cropTo(img)

        # flips the image
        img = cv2.flip(img, 1)

        # normalize the image and load it into an array that is the right format for keras
        normalized_img = (img.astype(np.float32) / 127.0) - 1
        data_for_model[0] = normalized_img

        # run inference
        prediction = model.predict(data_for_model)
        prediction = prediction[0]
        f0 = prediction[0]
        f1 = prediction[1]

        time.sleep(1)
        handUp = False
        if f0 > 0.70:
            print(counter)
            handUp = True
            if handUp:
                counter += 1
                os.system(f"say {counter}")
            handUp = False
            time.sleep(1)
        cv2.imshow("frame", img)
        if cv2.waitKey(1) == 27:
            break


cv2.destroyAllWindows()
