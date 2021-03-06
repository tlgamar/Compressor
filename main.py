from flask import Flask,request,render_template,redirect
import os
from compressor import randomg
from werkzeug.utils import secure_filename

try:
	os.mkdir("tmp")
except:
	print("Already")

app = Flask(__name__)

@app.route('/home', methods = ["GET"])
def senHTML():
	return render_template('index.html')

@app.route('/upload', methods = ["POST"])
def upload_image():
	image = request.files['file']
	image.save("tmp/"+image.filename)
	img = randomg("tmp/"+image.filename)
	return "Program is working"

app.run(debug=True,port=2000)