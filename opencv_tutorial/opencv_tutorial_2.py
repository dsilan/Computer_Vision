import cv2
import argparse
import imutils
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="image path")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Image", gray)
#cv2.imshow("Edged", edged)
thresholding = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("thresholding", thresholding)

#find the contours/outlines
cnts = cv2.findContours(thresholding.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

#loop over the contours
for c in cnts:
    cv2.drawContours(output, [c], -1, (51, 51, 255), 3)
    cv2.imshow("Contours", output)

#text on the image
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10,25), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (51, 51, 255), 2)
cv2.imshow("Contours", output)

cv2.waitKey(0)