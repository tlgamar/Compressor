import os
from datetime import datetime
import cv2

img = cv2.imread("Original Photos/11737.jpg")
img_d = "Original Photos/11737.jpg"

timestamp = os.path.getctime(img_d)

foldername = datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y")
result = os.path.exists(foldername)
if result == False:
    os.makedirs(foldername)
    cv2.imwrite(os.path.join(foldername, f"{img}.jpg"),img)
else:
    cv2.imwrite(os.path.join(foldername, f"{img}.jpg"),img)
    