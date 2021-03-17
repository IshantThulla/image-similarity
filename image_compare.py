import cv2
import numpy as np
from matplotlib import pyplot as plt
Image1 = cv2.imread("eminem 1.jpg")
Image2 = cv2.imread("eminem 2.jpg")


mask = np.zeros(Image1.shape[:2],np.uint8)

sift = cv2.xfeatures2d.SIFT_create()
keypoint1, descriptor1 = sift.detectAndCompute(Image1,None)
keypoint2, descriptor2 = sift.detectAndCompute(Image2,None)

index_parameter = dict(algorithm = 0,trees = 5)
search_parameter = dict()
flann = cv2.FlannBasedMatcher(index_parameter,search_parameter)
matches = flann.knnMatch(descriptor1,descriptor2,k=2)

good_point_array = []
for i, j in matches:
    if i.distance < 0.75*j.distance:
        good_point_array.append(i)
resultant_match = cv2.drawMatches(Image1, keypoint1, Image2, keypoint2,good_point_array, None)

cv2.imshow("resultant_match",resultant_match)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,450,290)
cv2.grabCut(Image1,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = Image1*mask2[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()
