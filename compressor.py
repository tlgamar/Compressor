import cv2
import os
from datetime import datetime

def randomg(img_path):
    file_name = os.path.basename(img_path)
    # Getting the image's creation date
    timestamp = os.path.getctime(img_path)
    foldername = datetime.fromtimestamp(timestamp).strftime("%m-%Y")
    # Getting ready for resizing
    img_const = cv2.imread(img_path)
    img = img_const
    path = os.path.join(foldername, f"{file_name}")
    
    ratio = img.shape[0]/img.shape[1]

    res_l = (3840, int(3840*ratio)) # Resolution for 4k photo
    res_m = (1280, int(1280*ratio)) # Resolution for 720p photo
    res_s = (640, int(640*ratio)) # Resolution for 480p photo
    foldername_exist = os.path.exists(f"photos/original/{foldername}")
    # Checking whether the given photo is 4k+ or not
    if(img.shape[0]>3840): # If the photo is larger than 4k resolution
        # Making 4k photo
        img = cv2.resize(img, res_l, interpolation = cv2.INTER_AREA)
        img_4k = img
        if foldername_exist == False:
            os.makedirs(f"photos/original/{foldername}")
            cv2.imwrite(f"photos/original/{path}",img_4k, [cv2.IMWRITE_JPEG_QUALITY, 100])
        else:
            cv2.imwrite(f"photos/original/{path}",img_4k, [cv2.IMWRITE_JPEG_QUALITY, 100])

    else: # If the photo is not larger than 4k
        # Saving Original photo
        if foldername_exist == False:
            os.makedirs(f"photos/original/{foldername}")
            cv2.imwrite(f"photos/original/{path}",img, [cv2.IMWRITE_JPEG_QUALITY, 100])
        else:
            cv2.imwrite(f"photos/original/{path}",img, [cv2.IMWRITE_JPEG_QUALITY, 100])
    foldername_exist = os.path.exists(f"photos/medium/{foldername}")
    # Making 720p photo
    resized_m = cv2.resize(img, res_m, interpolation = cv2.INTER_AREA)
    if foldername_exist == False:
        os.makedirs(f"photos/medium/{foldername}")
        cv2.imwrite(f"photos/medium/{path}",resized_m, [cv2.IMWRITE_JPEG_QUALITY, 60])
    else:
        cv2.imwrite(f"photos/medium/{path}",resized_m, [cv2.IMWRITE_JPEG_QUALITY, 60])
    foldername_exist = os.path.exists(f"photos/small/{foldername}")
    # Making 480p photo
    resized_s = cv2.resize(img, res_s, interpolation = cv2.INTER_AREA)
    if foldername_exist == False:
        os.makedirs(f"photos/small/{foldername}")
        cv2.imwrite(f"photos/small/{path}",resized_s, [cv2.IMWRITE_JPEG_QUALITY, 20])
    else:
        cv2.imwrite(f"photos/small/{path}",resized_s, [cv2.IMWRITE_JPEG_QUALITY, 20])