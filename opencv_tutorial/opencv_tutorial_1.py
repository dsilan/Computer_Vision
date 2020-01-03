import imutils
import cv2

#load the image and print dimensions
image = cv2.imread("../../images/ai_movie.jpg")
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
'''
#Resizing Images maintaining aspect ratio
r = 300 * w
dim = (300, int(h * r))
resized_ar = cv2.resize(image,dim)
cv2.imshow("Aspect Ratio Resized Image", resized_ar)
'''
#Resizing Images maintaining aspect ratio using IMUTILS
i_resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", i_resized)

#Rotating an image
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, -45, 1.0) #rotating 45 degrees clockwise
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated image", rotated)

#Rotating image using imutils
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)

#smoothing an image
blurred = cv2.GaussianBlur(image, (15, 15), 0) #larger kernel size would yield a more blurry image
cv2.imshow("Blurred", blurred)

#Drawing on an image
output = image.copy()
cv2.rectangle(output, (620,0), (800,190), (255,0,0), 2) 
cv2.imshow("2px thick blue rectangle surrounding the face",output)
cv2.waitKey(0)