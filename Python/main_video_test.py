import cv2
from ultralytics import YOLO
from gpiozero import Buzzer, LED
from time import sleep

buzzer = Buzzer(18)
led = LED(23)

model = YOLO('/home/pi/my_env/yolov8n.pt')

video_path = '/home/pi/my_env/KakaoTalk_20241104_023533638.mp4'

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Cannot open video file.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    detections = results[0].boxes
    
    if detections is not None and len(detections) > 0:
        print("Object detected!")
        buzzer.on()
        led.on()
    else:
        print("No object detected")
        buzzer.off()
        led.off()

    annotated_frame = results[0].plot()
    
    cv2.imshow('YOLO Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
