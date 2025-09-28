import cv2
import matplotlib.pyplot as plt
image = cv2.imread('dow.png')
image_rgb = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap = 'gray')
plt.title("GRAY image")
plt.show()
cropped_image = image[0:50,200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_image)
plt.title("Cropped Rgb image")
plt.show()