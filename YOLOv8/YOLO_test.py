from ultralytics import YOLO
import cv2

model=YOLO('../YOLO-Weights/yolov8n.pt')
results=model("/Users/whosameerarora/PycharmProjects/YOLO_v8/Images/image3.jpg", show=True)

cv2.waitKey(0)