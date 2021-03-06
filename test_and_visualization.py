# -*- coding: utf-8 -*-
"""Test and visualization

The image labels with their corresponding index number-

0.   'Jackfruit'
1.   'Mango field'
2.   'Pohela Boishakh'
3.   'Rice field'
4.   'Rickshaw'
5.   'River Boat'
6.   'Traffic Jam'
7.   'Village House'
8.   'churi'
9.   'flood'
10.  'fuchka'
11.  'mosque' 
12.  'nakshi pitha'
"""

import cv2
import tensorflow as tf
import matplotlib.pyplot as plt

#Function defining for the loaded model and image

def prepare(filepath):
    IMG_SIZE =256
    img_array = cv2.imread(filepath)  
    new_array= cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))  #resizing and making array
    return new_array.reshape(1,IMG_SIZE,IMG_SIZE,3).astype('float32')  #reshaping the image

model=tf.keras.models.load_model("/content/drive/MyDrive/model.hdf5") #loading model

test = ("/content/drive/MyDrive/Test/test/test (14).jpg") #calling test image
image=prepare(test)
image = image/255.0  #Normalize the image array

#Predicting the image

prediction = model.predict([image])

predicted_class_indices = np.argmax(prediction, axis = 1) #argmax for showing the predicted index value 
print(predicted_class_indices)

#Testing image visualization

im = cv2.imread(test) 
im_resized = cv2.resize(im, (256, 256), interpolation=cv2.INTER_LINEAR)  #resizing 

plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
plt.show()
