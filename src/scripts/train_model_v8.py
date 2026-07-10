from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(cfg="config.yaml", project="results/yolo_v8")
