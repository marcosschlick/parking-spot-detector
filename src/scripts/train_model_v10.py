from ultralytics import YOLO

# Load a pretrained model
model = YOLO("yolo10n.pt")

# Train the model on your custom config
model.train(cfg="config.yaml", project="results/yolo_v10")   