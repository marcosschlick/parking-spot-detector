from ultralytics import YOLO
import os

VERSION_PATHS = {
    "yolov8": "./results/yolo_v8/result/weights/best.pt",
    "yolov9": "./results/yolo_v9/result/weights/best.pt",
    "yolov10": "./results/yolo_v10/result/weights/best.pt",
    "yolov11": "./results/yolo_v11/result/weights/best.pt",
}

def load_model(version="yolov8"):
    model_path = VERSION_PATHS.get(version)
    if not model_path:
        supported_versions = ", ".join(VERSION_PATHS)
        raise ValueError(f"Unsupported model version '{version}'. Use one of: {supported_versions}")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found for {version}: {model_path}")

    model = YOLO(model_path)
    return model
