from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input

model=load_model('model_inception.h5')


img=image.load_img('Datasets/Category1.JPG',target_size=(224,224))
x=image.img_to_array(img)
x
x.shape

x=x/255
import numpy as np
x=np.expand_dims(x,axis=0)
img_data=preprocess_input(x)
img_data.shape



model.predict(img_data)
a=np.argmax(model.predict(img_data), axis=1)

print("Category of Image is:")

print(a)
