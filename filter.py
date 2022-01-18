import os
from datetime import datetime

img = "Original Photos/11737.jpg"

timestamp = os.path.getctime(img)
foldername = datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y")
result = os.path.exists(foldername)
if result == False:
    os.makedirs(foldername)
    os.path.join(foldername, img)
else:
    os.path.join(foldername, img)