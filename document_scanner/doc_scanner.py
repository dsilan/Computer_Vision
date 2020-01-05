import cv2
import imutils
import numpy as np 
from perspective.pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
#Step1: Detect Edges
image = cv2.imread("../../images/fis.jpg")
orig = image.copy()
ratio =  image.shape[0] / 500.0
image = imutils.resize(image, height=500)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_removed_noise = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray_removed_noise, 75, 200)
cv2.imshow("Gri fis", edged)

#Step2: Finding Contours
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)

#loop over the contours
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.002 * peri, True)

    
	# if our approximated contour has four points, then we
	# can assume that we have found our screen
    if len(approx) > 4:
        screenCnt = approx
        break
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)

#Step 3: Apply a Perspective Transform & Threshold

warped = four_point_transform(orig, screenCnt.reshape(8, 2) * ratio)
warped = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255

cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.waitKey(0)
cv2.destroyAllWindows()