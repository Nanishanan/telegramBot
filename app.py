from codecs import backslashreplace_errors
import cv2
import sys
import numpy as np
from PIL import Image

cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_lefteye_2splits.xml')

# sys.argv[1] = '1331956136'
img = cv2.imread('public/images/' + sys.argv[1] + '.jpg')
img2 = cv2.imread('public/images/' + sys.argv[1] + '.jpg')
# img = cv2.imread('public/images/1331956136.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=cascade_classifier.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=5)

print(faces)

for x, y, w, h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),-1)

x_a = faces[0][0]
y_a = faces[0][1]

x_a_1 = faces[1][0]
y_a_1 = faces[1][1]

img = cv2.line(img, (x_a,y_a), (x_a_1, y_a_1), (0,0,0), 4)

# resized=cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3)))

# foreground = Image.open('public/images/glass.png')
# foreground = foreground.resize((152,252), Image.ANTIALIAS)
# foreground = foreground.convert("RGBA")

# background = Image.open('public/images/'+sys.argv[1]+'.jpg')
# background = background.convert("RGBA")

# background.paste(foreground, (x_axis,y_axis), foreground)
# background.save("file.png", format="png")

# final = cv2.imread('file.png')

cv2.imshow("Swag Face", img)
# cv2.imshow("Deteced-face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()