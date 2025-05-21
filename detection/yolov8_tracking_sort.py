import cv2
import numpy as np
from ultralytics import YOLO
from sort import Sort

# Carrega o modelo YOLOv8
model = YOLO('yolov8n.pt')

# Abre o vídeo
video_path = 'assets/sample_video.mp4'
cap = cv2.VideoCapture(video_path)

# Verifica se o vídeo foi carregado corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Inicializa o rastreador SORT
tracker = Sort()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Faz inferência com YOLOv8
    results = model(frame)
    detections = results[0].boxes

    dets = []
    for box in detections:
        cls = int(box.cls[0])
        if cls == 3:  # COCO class 3 = "motorbike"
            x1, y1, x2, y2 = box.xyxy[0]
            conf = float(box.conf[0])
            dets.append([x1.item(), y1.item(), x2.item(), y2.item(), conf])

    dets_np = np.array(dets)
    tracks = tracker.update(dets_np)

    # Desenha as caixas rastreadas
    for track in tracks:
        x1, y1, x2, y2, track_id = track.astype(int)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, f'Moto #{track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow("FleetZone - Rastreamento YOLOv8 + SORT", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
