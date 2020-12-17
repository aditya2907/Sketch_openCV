import cv2
import numpy as np 
import scipy.ndimage

start_img = cv2.imread("/home/rogue/python/Sketch/virat.jpg", cv2.IMREAD_COLOR)

#start_img.shape(196, 160, 30)

def grayscale(rgb): return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

gray_img = grayscale(start_img)
inverted_img = 255-gray_img

blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img,sigma=5)
def dodge(front,back): 
    result=front*255/(255-back)  
    result[result>255]=255 
    result[back==255]=255 
    return result.astype('uint8')

final_img= dodge(blur_img,gray_img)
cv2.imshow("Image", start_img)
cv2.imshow("Sketch", final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

