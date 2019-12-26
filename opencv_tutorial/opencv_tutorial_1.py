import imutils
import cv2

#load the image and print dimensions
image = cv2.imread("./ai_movie.jpg")
(h, w, d)=image.shape
print(" width={},height={}, depth={}".format(w,h,d))
cv2.imshow("Image",image)

#openCV still maintains BGR color space as standard
#colors of specific pixel
(B, G, R) = image[100, 50] #height = 100; width = 50
print("R={}, G={}, B={}".format(R, G, B))

#ROI - array slicing
#image[startY:endY, startX:endX]
roi = image[0:190, 620:800] #width=620-800 height=0-190
cv2.imshow("ROI",roi)

#Resizing Images ignoring aspect ratio
resized = cv2.resize(image,(200,200)) #width, height
cv2.imshow("Resized Image", resized)

#Resizing Images maintaining aspect ratio
r = 300 * w
dim = (300, int(h * r))
#this may give an error if the image size is too big
#resized_ar = cv2.resize(image,dim)
#cv2.imshow("Aspect Ratio Resized Image", resized_ar)

#Resizing Images maintaining aspect ratio using IMUTILS
i_resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", i_resized)
cv2.waitKey(0)