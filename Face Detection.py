# Importing OpenCV package
import cv2
  
# Reading the image
print("Enter the name or path to the image")
img = cv2.imread(input())
  
# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
haar_cascades = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
haar_cascadess = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
haar_cascadesss = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
haar_cascades1 = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
# Applying the face detection method on the grayscale image
eye_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
face = haar_cascades.detectMultiScale(gray_img, 1.1, 9)
face1 = haar_cascadess.detectMultiScale(gray_img, 1.1, 9)
face2 = haar_cascadesss.detectMultiScale(gray_img, 1.1, 9)
eye2 = haar_cascades1.detectMultiScale(gray_img, 1.1, 9)
# Iterating through rectangles of detected faces
for (x, y, w, h) in eye_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
for (x, y, w, h) in face1:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
for (x, y, w, h) in face2:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
for (x, y, w, h) in eye2:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Detected faces', img)
  
cv2.waitKey(0)
