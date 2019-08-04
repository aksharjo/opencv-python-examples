import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)
"""laplacian filter"""
lap = cv2.Laplacian(img, cv2.CV_64F, ksize= 3)
lap = np.uint8(np.absolute(lap))
"""sobel flter"""
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)

"""canny edge detection"""
edge = cv2.Canny(img, 100, 200)

sobelx = np.uint8(np.absolute(sobelx))
sobely =  np.uint8(np.absolute(sobely))

sobelCombined = cv2.bitwise_or(sobelx,sobely)

titles = ['image' , 'Laplacian' , 'sobelx', 'sobely', 'sobelCombined','canny']
images = [img, lap, sobelx, sobely, sobelCombined, edge]

for i in range(6):
    plt.subplot(2, 3, i+1),  plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
