# CMPT 141 - Arrays
# Topic(s): Array Applications
# DEMO


import numpy as np
import skimage.data as skdata
import matplotlib.pyplot as plt


def draw_histogram(image):
    """
    draw histogram data of 8-bit grayscale image to new figure
    image: 8-bit grayscale image to compute histogram for
    """

    # create 1D array of histogram data (maps intensities to counts)
    # 8-bit images have intensities from 0 to 255 inclusive
    # image[ image == 0].size  # size of 1d array with intensities all equal to zero
    # for all intensities 0-255 inclusive
    histogram = [image[image == intensity].size for intensity in range(256)]

    # draw the histogram
    plt.figure("Histogram")
    plt.bar(range(256), histogram)
    plt.xlabel("Intensity")
    plt.ylabel("Number of Pixels")


# # load image & draw image
# image = skdata.camera()   # image is a 2D array
# # plt.gray()
# # plt.imshow(image)
# plt.imshow(image, cmap='gray', vmin=0, vmax=255)
#
# # compute & draw image's histogram
# draw_histogram(image)
#
#
# # # display all figures
# plt.show()


# ------------explore skills-----------
# things I want to mention

# histogram plot one-liner
# image = skdata.camera()   # image is a 2D array
# plt.hist(image.flatten(), bins=range(256))
# plt.show()

# Can we modify this image?
# image = skdata.camera()
# plt.imshow(255-image, cmap='gray', vmin=0, vmax=255)
# new_image = image.copy()
# new_image[new_image < 200] = 0
# plt.imshow(new_image, cmap='gray', vmin=0, vmax=255)

# plt.imshow(image[::5, ::5], cmap='gray', vmin=0, vmax=255)
# plt.show()

# how about colour image?
image = skdata.coffee()  # 3D array with shape (400, 600, 3) , 3: R G B
# print(image.shape)
# plt.imshow(image)

plt.imshow(image[:,:,0], cmap="Reds", vmin=0, vmax=255)

plt.show()