import numpy as np
import cv2
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import metrics
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import os

def image_to_feature_vector(image,size=(90,90)):#flattens the image into a 30,000-d feature vector
    return cv2.resize(image,(90,90))

data = []
labels = []

def add_data(imagePaths):
    for imagepath in os.listdir(imagePaths):
    image = cv2.imread(imagePaths + os.sep + imagepath)
    label = imagepath.split(os.path.sep)[-1].split(".")[0]
    features = image_to_feature_vector(image)
    data.append(features)
    labels.append(label)

add_data('/home/robotix/Desktop/FinalProject/Palms')
add_data('/home/robotix/Desktop/FinalProject/Fists')

le = LabelEncoder()
labels = le.fit_transform(labels)
data = np.array(data) / 255.0
labels = np_utils.to_categorical(labels,2)
print(data.shape)
(X_train, X_test, y_train, y_test) = train_test_split(
data, labels, test_size=0.25, random_state=42)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), strides=(1, 1),
                 activation='relu',
                 input_shape=(90, 90, 3)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(32, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dense(30, activation='relu'))
model.add(Flatten())
model.add(Dense(2, activation='relu'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics= [metrics.binary_accuracy])
model.fit(X_train, y_train,batch_size=64,nb_epoch=6,verbose=1)

score = model.evaluate(X_test, y_test, verbose=0)

print (score)
