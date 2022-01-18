from flask import Flask,request,render_template,redirect
import os
from compress import randomg
from werkzeug.utils import secure_filename

app = Flask(__name__)

# app.config["IMAGE_UPLOADS"] = "/Users/DELL/OneDrive/Desktop/bestone/static"
#app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPG","JPEG"]


print("dddd")

@app.route('/home', methods = ["GET"])
def senHTML():
	return render_template('index.html')


@app.route('/upload',methods = ["POST"])
def upload_image():
	image = request.files['file'].read()

	randomg(image)
 

print("dddsdsdsdsd")

#@app.route('/display/<filename>')
#def display_image(filename):
#	return redirect(url_for('static',filename = "/Images" + filename), code=301)


app.run(debug=True,port=2000)

print("starting")