
import cv2


container = cv2.open('~/PycharmProjects/FinalProjectRobotics/flower.mov')

for packet in container.demux():
    for frame in packet.decode():
        if frame.type == 'video':
            frame.to_image().save('/path/to/frame-%04d.jpg' % frame.index)
        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()