import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout

# Build a neural network model
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(3,)))
model.add(Dropout(.1))
model.add(Dense(1, activation='relu'))
model.compile(loss='mse', optimizer='adam')

# Create an XOR dataset
X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0]]).T

# Perform the training
model.fit(X, y, batch_size=4, nb_epoch=1000, verbose=1)

# Make predictions
print (model.predict(X))