import numpy as np
import cv2 as cv
import base64
import pymorse
import random
from PIL import Image
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import scipy.signal


destination_counter = 0
x = 36.5
y = 34
z = 17

update_array = np.zeros(shape=(64,64,3))


pic_counter = 0

# Parameters for a new waypoint target
params = {'x':x, 'y':y, 'z':z, 'yaw':1, 'tolerance':0.5}
params2 = {'x':-20, 'y':10, 'z':15, 'yaw':1, 'tolerance':0.5}
params3 = {'x':-25, 'y':5, 'z':5, 'yaw':1, 'tolerance':0.5}
params4 = {'x':-20, 'y':10, 'z':10, 'yaw':1, 'tolerance':0.5}
params5 = {'x':-48, 'y':-3, 'z':10, 'yaw':1, 'tolerance':0.5}
# was -45 - 3
params_list = [params,params2,params3,params4,params5]
width = 64
height = 64
depth = 4
bigness = 500

# Callback for getting altitude sensor data
def gotAltitude(data):
    print data['z']

# Callback for getting images from the videocamera
def gotImage(img):
    global update_array
    img = img['image']
    x = base64.b64decode(img)
    mat = np.frombuffer(x, dtype="uint8")
    img_mat = np.reshape(mat, (width, height, depth))
    img_mat = cv.cvtColor(img_mat, cv.COLOR_BGRA2RGBA)
    cv.namedWindow('image', cv.WINDOW_NORMAL)
    if bigness > 0:
      cv.resizeWindow('image', bigness, bigness)
    cv.imshow("image", img_mat)
    cv.waitKey(1)
#onyl call analyzie image when you want to and this can be called in the for loop 
#got image stores image in global
    update_array = img_mat
#    analyzeImage(img_mat)

def gray(img1):
    print "graying image"
    img = np.array(img1)
    new_img = np.round(0.21 * img[:,:,0] + .71 * img[:,:,1] + .07 * img[:,:,2])
    return new_img

def saveImage(img):
    img1 = normalize(img).astype(np.uint8)
    print "normalize"
    img2 = Image.fromarray(img1)
    pic_counter = 1
    print img2
    filename = "chimney" + str(destination_counter)+ ".png"
    print filename
    img2.save(filename)

def applyLap(gray):
    lap_matrix = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
    lap_applied = scipy.signal.convolve2d(gray, lap_matrix, mode='same', boundary='fill',fillvalue=0)
    print lap_applied
    img = (lap_applied)
    return img

def analyzeImage(img):
    #apply grayscale filter
    gray_img = gray(img)
    print gray_img
    #print "Grayscale image"
    #apply lap matrix
    final_img = applyLap(gray_img)
    print "save img"
    #save image
    saveImage(final_img)
    print "image saved"

def normalize(img):
    normal_img = []
    img1 = img.flatten()
    min_val = min(img1)
    max_val = max(img1)
    for i in img1:
        i = (255 * abs(i))/max_val
        normal_img.append(i)
    #print normal_img
    normal_img = np.array(normal_img)
    img1 = normal_img.reshape(64,64)
    print img1
    return img1

#create helper functions to save img, do convolution, open image

simu = pymorse.Morse()



# subscribes to updates from the Videocamera sensor by passing a callback
simu.robot.videocamera.subscribe(gotImage)

for i in params_list:

    # sends a destination
    simu.robot.waypoint.publish(i)

    # Leave a couple of millisec to the simulator to start the action
    simu.sleep(0.1)

    # waits until we reach the target
    while simu.robot.waypoint.get_status() != "Arrived":
      simu.sleep(0.2)
     
    print("Here we are!")
    destination_counter+=1
    simu.sleep(5.0)
    print(update_array)
    analyzeImage(update_array)
    


# Disconnect this client, but don't destroy the simulation
simu.close()
