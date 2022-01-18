<<<<<<< HEAD
import cv2
import glob

def randomg(image):
        img_org = cv2.imread(image)
        img = img_org

        # for Images in path:
        #         img_org = cv2.imread(Images)
        #         img = img_org
        #         cv2.imshow("Image", img)

        print("check")

        if(img.shape[0] > 3840):
                static_1 = img.shape[0] / 3840
                static_1_root = img.shape[1] / static_1
        else:
                static_1 = 3840 / img.shape[0]
                static_1_root =  static_1 / img.shape[1]

        if(img.shape[0] > 1280):
                static_2 = img.shape[0] / 1280
                static_2_root =  img.shape[1] / static_2 
        else:
                static_2 = 1280 / img.shape[0]
                static_2_root =  static_2 / img.shape[1]   

        if(img.shape[0] > 640):
                static_3 = img.shape[0] / 640
                static_3_root =  img.shape[1] / static_3
                
        else:
                static_3 = 640 / img.shape[0]
                static_3_root =  static_3 / img.shape[1]



        res_l = (3840, int(static_1_root)) # Resolution for 4k photo

        res_m = (1280, int(static_2_root)) # Resolution for 720p photo

        res_s = (640, int(static_3_root)) # Resolution for 480p photo

                # Checking whether the given photo is 4k+ or not
        print("ceee")
        if(img.shape[0]>3840 or img.shape[1]>2160): # If the photo is larger than 4k resolution
                # Making 4k photo

                img = cv2.resize(img, res_l, interpolation = cv2.INTER_LINEAR)
                img_const = img
                cv2.imwrite("Compressed Photos/4k_or_original/a.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 100])
                print("random")
                        # Making 720p photo
                resized_m = cv2.resize(img, res_m, interpolation = cv2.INTER_LINEAR)
                cv2.imwrite("Compressed Photos/720p/a.jpg", resized_m, [cv2.IMWRITE_JPEG_QUALITY, 60])
                img = img_const

                        # Making 480p photo
                resized_s = cv2.resize(img, res_s, interpolation = cv2.INTER_LINEAR)
                cv2.imwrite("Compressed Photos/480p/a.jpg", resized_s, [cv2.IMWRITE_JPEG_QUALITY, 20])


        else: # If the photo is not larger than 4k
                # Saving Original photo
                cv2.imwrite("Compressed Photos/4k_or_original/a.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 100])

                        # Making 720p photo
                resized_m = cv2.resize(img, res_m, interpolation = cv2.INTER_LINEAR)
                cv2.imwrite("Compressed Photos/720p/a.jpg", resized_m, [cv2.IMWRITE_JPEG_QUALITY, 60])
                img = img_org

                        # Making 480p photo
                resized_s = cv2.resize(img, res_s, interpolation = cv2.INTER_LINEAR)
                cv2.imwrite("Compressed Photos/480p/a.jpg", resized_s, [cv2.IMWRITE_JPEG_QUALITY, 20])

cv2.waitKey()
cv2.destroyAllWindows()
=======
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
>>>>>>> 1c8c0ba36caf0982bfeb86cbdae5bbfc17fd45fe
