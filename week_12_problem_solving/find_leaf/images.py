import numpy as np
import skimage.io as io
import skimage.segmentation as seg
import skimage.filters as filter
from scipy.ndimage import binary_fill_holes
import matplotlib.pyplot as plt

# 1: Load and scale the image
leaf_image = io.imread('image_0002.jpg')
leaf_image_normalized = leaf_image / 255.0
height = leaf_image.shape[0]
width = leaf_image.shape[1]
# io.imshow(leaf_image)
# io.show()
# exit()

# 2: Obtain colour image channels
red = leaf_image_normalized[:, :, 0]
green = leaf_image_normalized[:, :, 1]
blue = leaf_image_normalized[:, :, 2]

# 3: compute the greenness of each pixel
greenness = np.zeros([height, width], dtype=float)

# 3a: Loop-based solution to compute greenness
for r in range(0, height):
    for c in range(0, width):
        if red[r, c] + green[r, c] + blue[r, c] != 0:
            greenness[r, c] = green[r, c] / (red[r, c] + green[r, c] + blue[r, c])
        else:
            greenness[r, c] = 0

# 3b: Loopless solution to compute greenness

# below is simple, but throws an error: RuntimeWarning: invalid value encountered in true_divide
# greenness = green / (red + green + blue)

#  working loopless solution ?


# 4. Plot histogram of greenness
# F = plt.figure()
# H, edges = np.histogram(greenness, bins=256)
# plt.bar(range(256), H, edgecolor='none')
# plt.xlim(0, 255)
# plt.show()
# print(edges[100])

# 4. or use plt.hist to plot histogram
# F = plt.figure()
# plt.hist(greenness.flatten(), bins=256)
# plt.show()

# 5. Obtain a good threshold of "greennness".
# Pixels with greenness higher than T are probably part of a leaf.
T = filter.threshold_otsu(greenness)


# 6: Segment the image using the greenness threshold.
# segmentation = np.zeros([height, width], dtype=bool)

# 6a: Loop-based solution
# for r in range(0, height):
#     for c in range(0, width):
#         if greenness[r, c] > T:
#             segmentation[r, c] = True

# 6b: Loopless soloution
# segmentation = greenness > T

# fill holes using a library function
# segmentation = binary_fill_holes(segmentation)

# # 7: draw the segmentation on the original image
# # find the boundary of leaf
# segmentation_boundaries = np.zeros_like(segmentation).astype(bool)
# for i in range(1, segmentation_boundaries.shape[0]-1):
#     for j in range(1, segmentation_boundaries.shape[1]-1):
#         if (segmentation[i, j] and  # leaf True, 8 neighbours are not all leaf
#                 not (segmentation[i - 1, j]
#                      and segmentation[i + 1, j]
#                      and segmentation[i, j - 1]
#                      and segmentation[i, j - 1]
#                      and segmentation[i + 1, j + 1]
#                      and segmentation[i - 1, j - 1]
#                      and segmentation[i + 1, j - 1]
#                      and segmentation[i - 1, j + 1])):
#             segmentation_boundaries[i, j] = True


# # use the module function seg:
# segmentation_boundaries = seg.find_boundaries(segmentation)
#
# red[segmentation_boundaries] = 1.0
# green[segmentation_boundaries] = 0.0
# blue[segmentation_boundaries] = 0.0
# result = np.dstack([red, green, blue])  # stack three channels together to form a new 3-D array
# segfig = plt.figure()
# io.imshow(result)


# 8: Measure how close the segmentation is to the right answer
#
# # load the ground truth
# GT = io.imread('threshimage_0002.png').astype(bool)
#
# # Compute Dice Similarity Coefficient
# intersection = np.logical_and(segmentation, GT)
# area_seg = np.sum(segmentation)
# area_gt = np.sum(GT)
# area_intersect = np.sum(intersection)
# DSC = 2 * area_intersect / (area_seg + area_gt)
# print('The Dice similarity coefficient of the segmentation is: ', DSC)
#
#
# io.show()
