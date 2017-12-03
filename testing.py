import numpy as np
import keras as kr
from keras.datasets import mnist

#Load the data in 
(xTrain, yTrain), (xTest, yTest) = mnist.load_data()

xTrain = xTrain.reshape(xTrain.shape[0], xTrain.shape[1], xTrain.shape[2]).astype('float32')
xTest = xTest.reshape(xTest.shape[0], xTest.shape[1], xTest.shape[2]).astype('float32')

#Scale image to 255 pixels and check if there are pixels in the area or not 
xTrain = xTrain/255
xTest = xTest/255

#Print the final shape before testing it
print("Train matrix shape", xTrain.shape)
print("Test matrix shape", xTrain.shape)

yTrain = kr.utils.np_utils.to_categorical(yTrain)
yTest = kr.utils.np_utils.to_categorical(yTest)

#Building a linear stack of layers with the sequential model
model = kr.models.Sequential()
model.add(kr.layers.Dense(512, input_shape=(xTrain.shape[1], xTrain.shape[2])))
model.add(kr.layers.Flatten())
model.add(kr.layers.Activation('relu'))
model.add(kr.layers.Dropout(0.2))
model.add(kr.layers.Dense(10))
model.add(kr.layers.Activation('softmax'))

#Train the model
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

#Fit the model
model.fit(xTrain, yTrain, batch_size = 128, epochs = 20, verbose = 1)

#Loss and accuracy measurement 
loss, accuracy = model.evaluate(xTrain, yTrain, verbose=1)
print("\n\nLoss: %6.4f\tAccuracy: %6.4f" % (loss, accuracy))
prediction = np.around(model.predict(np.expand_dims(xTest[0], axis=0))).astype(np.int)[0]

#Training and saving of the model 
history = model.fit(X_train, Y_train,
          batch_size=128, epochs=1,
          verbose=2,
          validation_data=(X_test, Y_test))

model.save('mnist_model.h5')
print('Saved trained model')
