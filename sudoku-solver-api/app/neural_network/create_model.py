from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.utils import to_categorical
import numpy as np

(X_train, y_train), (X_test, y_test) = mnist.load_data()

import os
import cv2

X = []
y = []
for i in range(10):
    for d in os.listdir("./app/neural_network/assets/{}".format(i)):
        t_img = cv2.imread("./app/neural_network/assets/{}".format(i) + "/" + d)
        t_img = cv2.cvtColor(t_img, cv2.COLOR_BGR2GRAY)
        X.append(t_img)
        y.append(i)

X = np.array(X)
y = np.array(y)

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=21
)

X_train = X_train.reshape((X_train.shape[0], 28, 28, 1)).astype("float32")
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1)).astype("float32")

X_train = X_train / 255
X_test = X_test / 255

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
num_classes = y_test.shape[1]


def digit_recognition_model():
    model = keras.Sequential(
        [
            Conv2D(30, (5, 5), input_shape=(28, 28, 1), activation="relu"),
            MaxPooling2D(),
            Conv2D(15, (3, 3), activation="relu"),
            MaxPooling2D(),
            Dropout(0.2),
            Flatten(),
            Dense(128, activation="relu"),
            Dense(50, activation="relu"),
            Dense(num_classes, activation="softmax"),
        ]
    )

    model.compile(
        loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
    )
    return model


model = digit_recognition_model()
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=10)
scores = model.evaluate(X_test, y_test, verbose=0)

y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_test_classes = np.argmax(y_test, axis=1)

f1 = f1_score(y_test_classes, y_pred_classes, average="weighted")
print("F1-score (weighted):", f1)


print(scores)
model.save("./app/neural_network/digit_recognizer_model.keras")
