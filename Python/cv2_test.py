import cv2
import time

# image load
'''
image = cv2.imread('/home/pi/my_env/test.jpg')
cv2.imshow('Image',image)
cv2.waitKey(0)

cv2.destroyAllWindows()
'''

# camera connect
cap =cv2.VideoCapture(-1, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
time.sleep(5)

if not cap.isOpened():
    print('error: could not open camera')
else:
    print('camera successfully opened')
    
    for i in range(5):
        ret, frame = cap.read()
        if not ret:
            print(f'error: failed to cpature frame {i+1}')
        else:
            print(f'frame {i+1} captured successfully')
            
cap.release()


# camera stream
'''
cap =cv2.VideoCapture(0)
if not cap.isOpened():
    print('error: could not open camera')
else:
    print('camera successfully opened')
    
while True:
    ret, frame = cap.read()
    
    if not ret:
        print('Error: Failed to cap')
        break
    
    cv2.imshow('camera', frame)
    
    if cv2.watikey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''