import cv2
vidcap = cv2.VideoCapture('leftH_test.h264')
success, image= vidcap.read()
count = 0
num = 0

while success:
    if (count % 20 == 0):
        cv2.imwrite("leftH_%d.jpg" % num, image)
        num += 1
    success, image = vidcap.read()
    print('read a new frame: ', success)
    count +=1
    