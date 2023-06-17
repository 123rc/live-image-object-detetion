import cv2
cam=cv2.VideoCapture('http://192.168.1.7:8080/video')
cv2.namedWindow("Capture")
img_counter=0
while True:
    ret,frame=cam.read()
    if not ret:
        print("failed")
        break
    cv2.imshow("test",frame)

    k=cv2.waitKey(1)
    if k%256==27:
        print("Closing")
        break
    if k%256==32:
        img_name="opencv{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("{}written!".format(img_name))
        img_counter+=1

cam.release()
cv2.destroyAllWindows()

