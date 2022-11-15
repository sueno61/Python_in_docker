import cv2

# Load an color image
img = cv2.imread("src/Berry.jpg")

cv2.imshow("img", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.waitKey(1)
