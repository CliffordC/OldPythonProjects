import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import np_utils
from keras.datasets import mnist
from keras import metrics

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 784)
X_test = X_test.reshape(X_test.shape[0], 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)
#print(y_train.shape)
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(784,)))
model.add(Dropout(.1))
model.add(Dense(10, activation='softmax'))
#model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics= [metrics.categorical_accuracy])
model.fit(X_train, y_train,batch_size=64,nb_epoch=6,verbose=1)

score = model.evaluate(X_test, y_test, verbose=0)

print (score)
# print(model.predict(X_train[:1]))
# print(y_train)
# print(model.predict(X_test[:1]))
# print(y_test)
# from matplotlib import pyplot as plt
#
# plt.imshow(X_train[0])