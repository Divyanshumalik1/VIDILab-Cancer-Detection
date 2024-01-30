
import cv2

# Load the image
img = cv2.imread('output/00105.jpg')

# Invert the image using cv2.bitwise_not
img_neg = cv2.bitwise_not(img)

# Show the image
#cv2.imshow('negative',img_neg)
#cv2.waitKey(0)
# cv2.imwrite('neg.jpeg',img_neg)

# import cv2
import numpy as np
# image1 = cv2.imread('output/00105.jpg')

# image1 = cv2.bitwise_not(image1)
# Apply Gamma=2.2 on the normalised image and then multiply by scaling constant (For 8 bit, c=255)
gamma_two_point_two = np.array(255*(img_neg/255)**1,dtype='uint8')
# Similarly, Apply Gamma=0.4
gamma_point_four = np.array(255*(img_neg/255)**0.4,dtype='uint8')
# Display the images in subplots
# img3 = cv2.hconcat([gamma_two_point_two,gamma_point_four])

#img3 = cv2.add(gamma_two_point_two, gamma_point_four)

cv2.imshow('a2',gamma_two_point_two)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite('gamaneg.jpeg',img3)


# import cv2
# import numpy as np
# image1 = cv2.imread('output/00879.jpg')
# # Apply log transform
# img_log = np.log(image1+1)/(np.log(1+np.max(image1)))*255
# # Specify the data type
# img_log = np.array(img_log,dtype=np.uint8)
# # Display the image
# cv2.imshow('log_image',img_log )
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('logtransformimage.jpeg',img_log)