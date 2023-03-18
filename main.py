import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('../DATA/internal_external.png',0)
# plt.imshow(img, cmap='gray');
# plt.show()

# there are other contours besides RETR_CCOMP
# image, contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE) #doesnt work, only returns 2 parameters in my current version
contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

print(type(contours)) #should get type 'list'
print(len(contours)) #should be 22 contours, one for each of the internal dots on the image
print(hierarchy) #there is a hierchy for different internal contours, view array to see the 3rd index value to determine which

external_contours = np.zeros(img.shape)
internal_contours = np.zeros(img.shape)
face_contours = np.zeros(img.shape)
pizza_contours = np.zeros(img.shape)

for i in range(len(contours)):
    # is external contour?
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(external_contours, contours,i, 255, -1)
    # elif hierarchy[0][i][3] != -1:
    #     # can specify if the value is equal to 0 or 4 to find specific hierarchy of contours
    #     cv2.drawContours(internal_contours, contours, i, 255, -1)
    elif hierarchy[0][i][3] == 0:
        cv2.drawContours(face_contours, contours, i, 255, -1)
    elif hierarchy[0][i][3] == 4:
        cv2.drawContours(pizza_contours, contours, i, 255, -1)

plt.imshow(external_contours, cmap='gray');
plt.show()

# plt.imshow(internal_contours, cmap='gray');
# plt.show()

plt.imshow(face_contours, cmap='gray');
plt.show()

plt.imshow(pizza_contours, cmap='gray');
plt.show()