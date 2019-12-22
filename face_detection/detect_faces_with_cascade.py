import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

make_720p()

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w] #black-white effect for screen-shot
        roi_color = frame[y:y+h, x:x+w] #colorful screen-shot
        img_item = "my-image.png"

        #takes screen-shot
        cv2.imwrite(img_item, roi_color)

        #to draw rectangle around the face
        color = (255, 0, 0) #BGR
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)


    frame = rescale_frame(frame, percent=50)
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()