import cv2
import json
from ultralytics import YOLO

model = YOLO("yolov8l.pt")

cap = cv2.VideoCapture("traffic.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        continue

    results = model(frame)

    vehicle_count = 0
    pedestrian_count = 0

    for r in results:

        for box in r.boxes:

            cls = int(box.cls)

            if cls in [2,3,5,7]:
                vehicle_count +=1

            if cls == 0:
                pedestrian_count +=1

    data = {}

    try:
        with open("traffic_state.json") as f:
            data = json.load(f)
    except:
        pass

    data["vehicles"] = vehicle_count
    data["pedestrians"] = pedestrian_count

    with open("traffic_state.json","w") as f:
        json.dump(data,f,indent=2)

    cv2.imwrite("frame.jpg",frame)

    cv2.imshow("Traffic Detection",frame)

    if cv2.waitKey(1)==27:
        break
