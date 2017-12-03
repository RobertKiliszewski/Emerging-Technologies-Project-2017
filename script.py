import os, re
from flask import render_template, Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import base64

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('./images')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route("/")
def index():
     return render_template("index.html")


@app.route('/uploadFile', methods=['POST'])
def upload_file():
	f = request.files['image']
	image_string = base64.b64encode(f.read())
	tmp = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
	f.save(tmp)
	return 'file uploaded successfully'
	
@app.route('/download/', methods=['GET','POST'])
def download():
    imgstr = re.search(b'base64,(.*)', request.get_data()).group(1)
    with open('my_image.png','wb') as output:
        output.write(base64.decodebytes(imgstr))
    return 'res'
		
if __name__ == '__main__':
   app.run(debug = True)