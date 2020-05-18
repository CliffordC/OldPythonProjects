import PIL
import numpy as np
from PIL import Image
import glob
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import np_utils
from keras.datasets import mnist
from keras import metrics



pic_data = []
face_file_path = 'train/face/*.pgm'
nface_file_path = 'train/non-face/*.pgm'

def addPicToArray(label,path):
    i = 0
    for pic in glob.glob(path):
        img = Image.open(pic)
        img1 = np.array(img)
        arr = img1.reshape(-1)
        row_face = [i,label]
        f_arr = np.append(arr,row_face)
        pic_data.append(f_arr)
        i += 1

def normalize(arr):
    for row in arr:
        for y in row:
            pass
    return None


addPicToArray(1,face_file_path)
addPicToArray(0,nface_file_path)

image_size = len(pic_data)

# Build a neural network model
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(image_size,)))
model.add(Dropout(.1))
model.add(Dense(1, activation='relu'))
model.compile(loss='binary_crossentropy', optimizer='adam')

# Create your image dataset here...
X = 6777
y = 361

# Perform the training
model.fit(X, y, batch_size=32, nb_epoch=1000, verbose=1)

# Make predictions
print (model.predict(X))

addPicToArray(1,face_file_path)
addPicToArray(0,nface_file_path)
print(pic_data[1])