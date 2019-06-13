import numpy as np
import argparse
import cv2
import requests
import random

def closest_color(i):
    r, g, b = 0, 0, 0
    d = 200000
    r1,g1,b1 = i[2],i[1],i[0]
    for j in pallete:
        r2,g2,b2 = j[2],j[1],j[0]
        if d > ((r2-r1)*0.30) ** 2 + ((g2-g1)*0.59) ** 2 + ((b2-b1)*0.11) ** 2:
            if random.randint(0,255)%2:
                r, g, b = r2, g2, b2
            d = ((r2-r1)*0.30) ** 2 + ((g2-g1)*0.59) ** 2 + ((b2-b1)*0.11) ** 2
    return (r,g,b)
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
image = cv2.imread(args["image"],cv2.IMREAD_COLOR)
r = requests.get("http://api.noopschallenge.com/hexbot?count=40")

h,w,x = image.shape

pallete = []
for i in r.json()['colors']:
    pallete.append((int(i['value'][1:3], 16), int(
        i['value'][3:5], 16), int(i['value'][5:7], 16)))
print pallete

canv = np.full((h, w, 3), 0, dtype=np.uint8)
print pallete
for i in range(h):
    for j in range(w):
        t = closest_color(image[j][i])
        cv2.circle(canv,(i,j),3,t)
    print h - i
cv2.imshow("image", image)
cv2.imshow("image1", canv)
cv2.waitKey(0)
