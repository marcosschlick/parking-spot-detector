import cv2
import os
from ultralytics import YOLO

# Find the most recent directory in the results folder
results_dir = "./results"  
all_subdirs = [os.path.join(results_dir, d) for d in os.listdir(results_dir) 
               if os.path.isdir(os.path.join(results_dir, d)) and d.startswith("result_")]
latest_dir = max(all_subdirs, key=os.path.getmtime)

# Build the path to the best model
MODEL_PATH = os.path.join(latest_dir, "weights", "best.pt")

# load trained model
model = YOLO(MODEL_PATH)

# select camera (0 for default, 1 for secondary)
CAMERA_INDEX = 0  

camera = cv2.VideoCapture(CAMERA_INDEX)
is_running = True

if not camera.isOpened():
    print(f"Error: could not open camera {CAMERA_INDEX}")
    is_running = False

while is_running:
    status, frame = camera.read()
    
    if not status or cv2.waitKey(1) & 0xFF == ord('q'):
        is_running = False
        continue
    
    # run inference on the frame
    results = model(frame, verbose=False)

    detections = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            confidence = float(box.conf)
            bbox = box.xyxy[0].tolist()  # [x_min, y_min, x_max, y_max]
            
            detections.append({
                "class": result.names[class_id],
                "confidence": confidence,
                "bbox": bbox
            })
    
    # visualize results on frame
    annotated_frame = results[0].plot()
    cv2.imshow("HotWheels Parking Spot Detector", annotated_frame)

camera.release()
cv2.destroyAllWindows()