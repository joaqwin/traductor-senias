import cv2
import os

from tensorflow import keras

from keras_preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras.layers import Convolution2D, MaxPooling2D
from keras import backend as K
from keras.callbacks import TensorBoard
from keras.optimizers import Adam

K.clear_session()

datos_training = "/home/usuario/PycharmProjects/pythonProject/Photos/training"
datos_validation = "/home/usuario/PycharmProjects/pythonProject/Photos/validation"

#parametros
epochs = 15
height, length = 200, 200
batch_size = 1
steps = 300 / 1
steps_validation = 300 / 1
filtersconv1 = 32
filtersconv2 = 64
filtersconv3 = 128
size_filter2 = (3, 3)
size_filter3 = (2, 2)
size_filter1 = (4, 4)
size_pool = (2, 2)
classes = 5
lr = 0.00005 #learning rate

#pre-procesamiento de las imagenes
preprocessing_training = ImageDataGenerator(rescale =1. / 255,
                                            shear_range = 0.3,
                                            zoom_range = 0.3,
                                            horizontal_flip = True)

preprocessing_validation = ImageDataGenerator(rescale =1. / 255)

image_training = preprocessing_training.flow_from_directory(datos_training, target_size=(height, length), batch_size=batch_size, class_mode='categorical')

image_validation = preprocessing_validation.flow_from_directory(datos_validation, target_size=(height, length), batch_size=batch_size, class_mode ='categorical')

cnn = Sequential()
cnn.add(Convolution2D(filtersconv1, size_filter1, padding='same', input_shape=(height, length, 3), activation ='relu'))

cnn.add(MaxPooling2D(pool_size=size_pool))

cnn.add(Convolution2D(filtersconv2, size_filter2, padding ='same', activation ='relu'))

cnn.add(MaxPooling2D(pool_size=size_pool))

cnn.add(Convolution2D(filtersconv3, size_filter3, padding ='same', activation='relu'))
cnn.add(MaxPooling2D(pool_size=size_pool))

cnn.add(Flatten())
cnn.add(Dense(650, activation='sigmoid'))
cnn.add(Dropout(0.5))
cnn.add(Dense(classes, activation='softmax'))

#optimizer = keras.optimizers.Adam(learning_rate=lr)
cnn.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

Board = TensorBoard(log_dir="/home/usuario/PycharmProjects/pythonProject/Board")
cnn.fit(image_training, steps_per_epoch=steps, epochs=epochs, validation_data=image_validation, validation_steps=steps_validation, callbacks=[Board])

cnn.save('Modelo.h5')
cnn.save_weights('pesos.h5')
