# Necessarry imports
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

#All of the Keras imports to help us with MNIST and Neural Network
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

#Load The data in 
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#Print the datas shape before doing any changes to it 
print("X_train shape", X_train.shape)
print("y_train shape", y_train.shape)
print("X_test shape", X_test.shape)
print("y_test shape", y_test.shape)

#Building the input vector from the 28x28 pixels
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

#Normalizing the data in order to help testing it 
X_train /= 255
X_test /= 255

#Print the final shape before testing it
print("Train matrix shape", X_train.shape)
print("Test matrix shape", X_test.shape)

print(np.unique(y_train, return_counts=True))

n_classes = 10
print("Shape before one-hot encoding: ", y_train.shape)
Y_train = np_utils.to_categorical(y_train, n_classes)
Y_test = np_utils.to_categorical(y_test, n_classes)
print("Shape after one-hot encoding: ", Y_train.shape)

# building a linear stack of layers with the sequential model
model = Sequential()
model.add(Dense(512, input_shape=(784,)))
model.add(Activation('relu'))                            
model.add(Dropout(0.2))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(10))
model.add(Activation('softmax'))

#Compiling the model after sequentilizing it
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

#Training and saving of the model 
history = model.fit(X_train, Y_train,
          batch_size=128, epochs=1,
          verbose=2,
          validation_data=(X_test, Y_test))

model.save('mnist_model.h5')
print('Saved trained model')

