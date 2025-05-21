import cv2
import numpy as np

# Caminhos dos modelos MobileNet
prototxt = 'detection/MobileNetSSD_deploy.prototxt.txt'
model = 'detection/MobileNetSSD_deploy.caffemodel'

# Classe alvo
TARGET_CLASS = 'motorbike'

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tvmonitor"]

net = cv2.dnn.readNetFromCaffe(prototxt, model)
video = cv2.VideoCapture('assets/sample_video.mp4')

trackers = cv2.MultiTracker_create()
frame_index = 0
DETECTION_INTERVAL = 30  # Executa detecção a cada 30 frames

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame_index += 1

    if frame_index % DETECTION_INTERVAL == 0:
        trackers = cv2.MultiTracker_create()
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
        net.setInput(blob)
        detections = net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                class_id = int(detections[0, 0, i, 1])
                if CLASSES[class_id] == TARGET_CLASS:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    tracker = cv2.TrackerKCF_create()
                    trackers.add(tracker, frame, (startX, startY, endX - startX, endY - startY))
    else:
        success, boxes = trackers.update(frame)
        for box in boxes:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("FleetZone - Rastreamento OpenCV", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
