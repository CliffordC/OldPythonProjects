 # Import libraries
import numpy as np
import cv2 as cv
import pymorse
import math
import base64
pic_counter = 0
change_x = 0
speed = 0
width = 256
height = 256
depth = 4
bigness = 500

delay_counter = 0


previous_image = np.zeros(shape=(256,256,3))
current_image = np.zeros(shape=(256,256,3))


# Load an image from a file
#img = cv.imread('test.jpg')
# Create an ORB feature detector
orb = cv.ORB_create()

def getKeypoints(img):
    global orb
    print "Getting points"
    img1 = cv.imwrite('keypoints.jpg',img)
    img2 = cv.imread('keypoints.jpg', img1)
    #print "img is read"
    # Get keypoints and descriptors for this image
    kp, desc = orb.detectAndCompute(img2, None)
    print "got da points"
    return kp, desc

def showKeypoints(img):
    # Draw little circles for the detected keypoints
    kp_color = (255, 0, 0)
    kp_size = 10
    for point in kp:
        x, y = point.pt
        cv.circle(img, (int(x), int(y)), kp_size, kp_color, -1)
    # Save the image with keypoints drawn on
    cv.imwrite("keypoints.jpg", img)
    # Open a window to show the image
    cv.imshow("image", img)
    # Wait until the user presses a key to close the window
    cv.waitKey(0)

def matchKeypoints(img,img2):
    kp, desc = getKeypoints(img)
    kp2, desc2 = getKeypoints(img2)
    # Create a brute-force matcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match keypoint descriptors found in two successive frames of video
    matches = bf.match(desc, desc2)
    # Put the matches in sorted order so the first ones are the closest (best matches)
    matches = sorted(matches, key = lambda x:x.distance)
    # Create an image showing lines that connect the matched keypoints
    img_matched = cv.drawMatches(img, kp, img2, kp2,
                               matches[:num_matches],None,
                               flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

def analyzeKeypoints(img, img2):
    global change_x
    global speed
    kp, desc = getKeypoints(img)
    print kp
    kp2, desc2 = getKeypoints(img2)
    print kp2
    for point in kp:
        for point2 in kp2:
            #print "HERERERERRE"
            x, y = point.pt
            #print "First X: ", x ,"First Y: ", y
            x2, y2 = point2.pt
            #print "Second X: ", x2, "Second Y: ",y2
            change_x = x2-x
            speed = math.sqrt( pow(change_x,2))
            print "Speed: " , speed
            if change_x > 0:
                print "Moving Right"
            if change_x < 0:
                print "Moving left"
            else:
                print "Standing Still"

def saveImage(img):
    img1 = Image.fromarray(img).astype(np.uint8)
    #pic_ounter+=1
    filename = "chimney" + str(pic_counter)+ ".png"
    print filename
    img1.save(filename)


def gotImage(img):
    global delay_counter
    global previous_image
    global current_image
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
    print delay_counter
    #if delay_counter >10:
    previous_image = current_image
    current_image = img_mat
    analyzeKeypoints(previous_image, current_image)
    #delay_counter = 0
    #delay_counter+=1

simu = pymorse.Morse()

simu.robot.videocamera.subscribe(gotImage)

simu.sleep(0.1)

while True:
    simu.sleep(0.2)

simu.sleep(5)


simu.close()
