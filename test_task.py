import cv2
import numpy as np

mat = 10,10
image = cv2.imread("test_images/test_image3.jpg")
occupied_grids = []
objects={}
(x,y,z) = image.shape

##HSV
img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask2 = cv2.inRange(img_hsv, lower_blue, upper_blue)

lower_green = np.array([50,100,100])
upper_green = np.array([70,255,255])
mask3 = cv2.inRange(img_hsv, lower_green, upper_green)

lower_yellow = np.array([20,240,240]) 
upper_yellow = np.array([40,255,255])
mask4 = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

mask=mask4+mask3+mask2+mask1+mask0

output_img = image.copy()
output_img[np.where(mask==0)] = 0

output_hsv = img_hsv.copy()
output_hsv[np.where(mask==0)] = 0
bgr_out=cv2.cvtColor(output_hsv,cv2.COLOR_HSV2BGR)

##Loop for Shape,occupied objets,colour....MAHA-LOOP
for i in range (10):
    for j in range (10):
        img1=image[(((j*x)/10)):((((j+1)*x)/10)),(((i*y)/10)):((((i+1)*y)/10)),:]
        (p,q,s)=img1.shape
        (B,G,R)=img1[p/2,q/2]
        if ( not (B>200 and G>200 and R>200)):
            occupied_grids = occupied_grids + [(i+1,j+1)]
            if (not (B<50 and G<50 and R<50)):
                img1=mask[(((i*x)/3)+8):((((i+1)*x)/3)-8),(((j*y)/3)+8):((((j+1)*y)/3)-8)]
                contours,h = cv2.findContours(img1,1,2)
                for cnt in contours:
                    approx = cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
                    if len(approx)==3:
                        board_shape[position]="Triangle"
                    elif len(approx)==4:
                        board_shape[position]="4-sided"
                    elif len(approx) > 7:
                        board_shape[position]="Circle"
                        break
                    else :
                        board_shape[position]="none"
                        position=position+1
 #print board_shape
             gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
             ret,thresh = cv2.threshold(gray,127,255,1)
             contours,h = cv2.findContours(thresh,1,2)
             cnt=contours[0]
             if (B<10 and G<10 and R>200):
                 colour="red"
             if (B<10 and R<10 and G>200):
                 colour="green"
             if (G<10 and R<10 and B>200):
                 colour="blue"
             if (B<10 and R>200 and G>200):
                 colour="yellow"
print occupied_grids
