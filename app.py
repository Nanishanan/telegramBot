from turtle import width
import cv2
import sys
from PIL import Image
from cv2 import rectangle

# cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_lefteye_2splits.xml')
# cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
cascade_classifier = cv2.CascadeClassifier('haarcascades/frontalEyes35x16.xml')
cascade_classifier1 = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
mouth_cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_mcs_mouth.xml')

# sys.argv[1] = '1331956136'
img = cv2.imread('public/images/' + sys.argv[1] + '.jpg')
img2 = cv2.imread('public/images/' + sys.argv[1] + '.jpg')
img3 = cv2.imread('public/images/' + sys.argv[1] + '.jpg')

# img = cv2.imread('public/images/1331956136.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

faces=cascade_classifier.detectMultiScale(gray_img, scaleFactor=1.3,minNeighbors=5)
faces1=cascade_classifier1.detectMultiScale(gray_img2, scaleFactor=1.1,minNeighbors=3)
mouth=mouth_cascade_classifier.detectMultiScale(gray_img3, scaleFactor=1.1,minNeighbors=3)

# print("F1", faces)
# print("F2", faces1)
# print("Mouth", mouth[0])
# print("Mouth", mouth[1])
# print("Mouth", mouth[2])
# print("Mouth", mouth[3])

try:
    x,y,w,h = faces[1]
except:
    x,y,w,h = faces[0]

x1,y1,w1,h1 = faces[0]

a,b,c,d = faces1[0]
# print(faces1)

img=cv2.rectangle(img,(x,y),(x1+w1,y1+h1),(0,0,0),2)

# Draw rectangle around the faces
# for (x2, y2, w2, h2) in faces1:
#     cv2.rectangle(img2, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 2)

# for (x2, y2, w2, h2) in faces:
#     cv2.rectangle(img, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 2)

glasses = cv2.imread("public/images/glasses.png", cv2.IMREAD_UNCHANGED)
glasses = cv2.cvtColor(glasses,cv2.COLOR_BGRA2RGBA)
glasses = cv2.resize(glasses,((c),(h)), interpolation = cv2.INTER_LINEAR)

for i in range(glasses.shape[0]):
        for j in range(glasses.shape[1]):
            if(glasses[i,j,3]>0):
                img2[y+i, a+j,:]=glasses[i,j,:-1]


#Draw Rectangle around Mouth
m,o,u,t = mouth[1]
# m,o,u,t = 277, 181, 64, 39
# img3=cv2.rectangle(img3, (m+int(u/2),o+int(t/2)), (m+u, o+t), (255,0,0), 2)
img3=cv2.rectangle(img3, (m,o ), (m+u, o+t), (255,0,0), 2)
# for m,o,u,t in mouth:
#     img3=cv2.rectangle(img3, (m,o), (m+u, o+t), (255,0,0), 2)

mouth_piece = cv2.imread('public/images/mouth.png', cv2.IMREAD_UNCHANGED)
mouth_piece = cv2.cvtColor(mouth_piece, cv2.COLOR_BGR2RGBA)
mouth_piece = cv2.resize(mouth_piece,(u,(t-15)), interpolation = cv2.INTER_LINEAR)

print(mouth_piece.shape)
for i in range(mouth_piece.shape[0]):
        for j in range(mouth_piece.shape[1]):
            if(mouth_piece[i,j,3]>0):
                img3[o+int(t/2)+i, m+int(u/2)+j,:]=mouth_piece[i,j,:-1]

# cv2.imwrite("public/out/"+sys.argv[1]+'.jpg', img2)
# cv2.imshow("Swag Face", img2)
# cv2.imshow("Swag Faces", img)
cv2.imshow("Swag Faces", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()