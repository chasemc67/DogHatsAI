from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.layers import Dense
import numpy as np

base_model = ResNet50(weights='imagenet', include_top=False)
x = base_model.output       

# look at what removing the top does, compare that with selecting a lower layer directly
# pop some fully-connected layers on top, which have the right number of output layers based on training data
x = Dense(1024, activation='relu')(x)   # not sure if 1024 is the right number here. also not sure on activation    
predictions = Dense(4, activation='relu')(x)

# this is the model we will train
model = Model(inputs=base_model.input, outputs=predictions)

# first: train only the top layers (which were randomly initialized)
# (freeze all convolutional ResNet50 layers)
# if performance isn't good, then we can unfreeze these
for layer in base_model.layers:
    layer.trainable = False


# compile the model (should be done *after* setting layers to non-trainable)
# optomizer and loss function might need to be custom here. Loss function needs to account for non-dog update
model.compile(optimizer='SGD', loss='categorical_crossentropy')


# train the model
# get training samples
# get training labels with preProcess_imageMonkey
# model.fit(samples, labels, batch_size=32, epochs=10)

# save the model
# print("[INFO] serializing network...")
# model.save(args["model"])
# # save the label binarizer to disk
# print("[INFO] serializing label binarizer...")
# f = open(args["labelbin"], "wb")
# f.write(pickle.dumps(lb))
# f.close()

# Evaluate the model with model.evaluate, or model.predict 