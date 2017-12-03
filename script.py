import flask
import re, base64
from flask import Flask, request, jsonify
from scipy.misc import imread, imresize
import keras as kr
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def uploadImage():
    #Data from the image is stored in the data variable 
    data = request.get_data()

    #remove what we dont need in 'data' and store it in img
    img = re.search(b'base64,(.*)', data).group(1)
    with open('./images/uploaded-img.png','wb') as fh:
        fh.write(base64.b64decode(img))
    
    img_bytes = imread('./images/uploaded-img.png', mode ='L')
    img_bytes = np.invert(img_bytes)
    img_bytes = imresize(img_bytes, (28,28))

    new_predict = np.ndarray.flatten(np.array(img_bytes)).reshape(1, 28, 28).astype('float32')
    new_predict = new_predict / 255
    pred = newPredict(new_predict)

    #Number prediction
    return pred

def newPredict(f):

    #Previously saved model is loaded in 
    model = kr.models.load_model("model.h5")
    
    #Predict what there is 
    prediction = model.predict(f)

    response = np.array_str(np.argmax(prediction))
    return response


if __name__ == '__main__':
    app.run() 