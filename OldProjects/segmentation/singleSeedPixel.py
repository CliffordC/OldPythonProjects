#Author Clifford Chirwa
import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Opens up the image, change the text in quotation for a different image
pic = Image.open("ducky.jpg").convert("L")
HEIGHT,WIDTH = pic.size
img1 = np.array(pic).astype(np.uint8) #makes the image into an array

#Starts an array for where the new image will be placed
segmented_img = np.zeros(shape=(WIDTH, HEIGHT))
region_threshold = 240

#An array for keeping track of visited pixels
visited = np.zeros((WIDTH, HEIGHT))

#Changes the pixel value of a pixel with the greyscale value of region_threshold to white or 255
def regionGrowth(row,column,x,y):
    global img1
    row = row + x
    column = column + y
    check = (column >= 0) & (row >= 0) & (column < HEIGHT) & (row < WIDTH)
    if check and visited[row][column] == 0:
        visited[row][column] = 1
        if img1[row][column] <= region_threshold:
            segmented_img[row][column]=(255)
    else:
        return
    regionGrowth(row,column,1,0)
    regionGrowth(row,column,0,1)

regionGrowth(1,0,0,0)
new_pic = Image.fromarray(segmented_img)
new_pic.show()
