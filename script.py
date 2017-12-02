import os 
from flask import render_template, Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('./images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route("/")
def index():
     return render_template("index.html")

@app.route('/uploader', methods=['POST'])
def upload_file():
	f = request.files['image']
	tmp = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
	f.save(tmp)
	return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)