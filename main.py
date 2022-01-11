import cv2

img_org = cv2.imread('Original Photos/11737.jpg', cv2.IMREAD_UNCHANGED)
img = img_org

res_l = (3840, 2160) # Resolution for 4k photo
res_m = (1280, 720) # Resolution for 720p photo
res_s = (640, 360) # Resolution for 480p photo

# Checking whether the given photo is 4k+ or not
if(img.shape[0]>3840 or img.shape[1]>2160): # If the photo is larger than 4k resolution
    # Making 4k photo
    img = cv2.resize(img, res_l, interpolation = cv2.INTER_AREA)
    img_const = img
    cv2.imwrite("Compressed Photos/4k_or_original/a.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 100])
    
    # Making 720p photo
    resized_m = cv2.resize(img, res_m, interpolation = cv2.INTER_AREA)
    cv2.imwrite("Compressed Photos/720p/a.jpg", resized_m, [cv2.IMWRITE_JPEG_QUALITY, 60])
    img = img_const

    # Making 480p photo
    resized_s = cv2.resize(img, res_s, interpolation = cv2.INTER_AREA)
    cv2.imwrite("Compressed Photos/480p/a.jpg", resized_s, [cv2.IMWRITE_JPEG_QUALITY, 20])


else: # If the photo is not larger than 4k
    # Saving Original photo
    cv2.imwrite("Compressed Photos/4k_or_original/a.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 100])

    # Making 720p photo
    resized_m = cv2.resize(img, res_m, interpolation = cv2.INTER_AREA)
    cv2.imwrite("Compressed Photos/720p/a.jpg", resized_m, [cv2.IMWRITE_JPEG_QUALITY, 60])
    img = img_org

    # Making 480p photo
    resized_s = cv2.resize(img, res_s, interpolation = cv2.INTER_AREA)
    cv2.imwrite("Compressed Photos/480p/a.jpg", resized_s, [cv2.IMWRITE_JPEG_QUALITY, 20])

cv2.waitKey()
cv2.destroyAllWindows()