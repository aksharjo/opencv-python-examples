import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread("messi5.jpg")
b , g, r = cv.split(img)

cv.imshow("img", img)
cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)

plt.hist(b.rave1(), 256, [0, 256])
plt.hist(g.rave1(), 256, [0, 256])
plt.hist(r.rave1(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
