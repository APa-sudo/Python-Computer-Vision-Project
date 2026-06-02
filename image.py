import cv2

img = cv2.imread("Final_Project/shirtificate.png",1)

img = cv2.resize(img,(400,400)) #interms of pixels

img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('Image',img) #first param is window name/title

cv2.waitKey(0) #wait for user to press any key. 0 signifies an infinite amount of time (time in milliseconds)

cv2.destroyAllWindows()

# -1, cv2.IMREAD_COLOR: Loads a color image. Any transparency of image will be ignored. This is default flag
# 0, cv2.IMREAD_GREYSCALE: loads image in greyscale
# 1, cv2.IMREAD_UNCHNAGED: Loads image as such inclucding alpha channel

