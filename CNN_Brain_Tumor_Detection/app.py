import os
import numpy as np
import cv2
from keras.models import load_model
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)


model = load_model('model.keras')
print('Model loaded. Check http://127.0.0.1:5000/')


def get_className(classNo):
    if classNo == 0:
        return "Glioma tumor"
    elif classNo == 1:
        return "Meningioma tumor"
    elif classNo == 2:
        return "No tumor"
    elif classNo == 3:
        return "Pituitary tumor"


def getResult(img):
    img = cv2.imread(img)
    img = cv2.resize(img, (240, 240))
    img = np.expand_dims(img, axis=0)
    result = model.predict(img)
    result = np.argmax(result)
    return result


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        value = getResult(file_path)
        result = get_className(value)
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)
