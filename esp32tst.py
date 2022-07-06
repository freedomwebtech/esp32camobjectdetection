import urllib.request
import time
import numpy as np
import cv2

url='http://192.168.43.207/cam-hi.jpg'

time.sleep(0.1)


while True:
    # Use urllib to get the image from the IP camera
    imgResp = urllib.request.urlopen(url)
    
    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    # Finally decode the array to OpenCV usable format ;) 
    image = cv2.imdecode(imgNp,-1)

    
    img = cv2.resize(image,(640,480))
    cv2.imshow("Frame", img);
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
       break
cap.release()
cv2.destroyAllWindows()