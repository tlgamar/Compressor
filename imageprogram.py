import cv2
import glob

def randomg(img_path):

        img = cv2.imread(img_path)
        img_org = img
        print(img_path)
        # for Images in path:
        #         img = img_org
        #         cv2.imshow("Image", img)

        print("check")

        if(img.shape[0] > 3840):
                static_1 = img.shape[0] / 3840
                static_1_root = img.shape[1] / static_1
        else:
                static_1 = img.shape[0] / 3840
                static_1_root = img.shape[1] / static_1

        if(img.shape[0] > 1280):
                static_2 = img.shape[0] / 1280
                static_2_root =   img.shape[1] / static_2
        else:
                static_2 = img.shape[0] / 1280
                static_2_root = img.shape[1] / static_2

        if(img.shape[0] > 640):
                static_3 = img.shape[0] / 640
                static_3_root = img.shape[1] / static_3
                
        else:
                static_3 = 640 / img.shape[0]
                static_3_root = img.shape[1] / static_3



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