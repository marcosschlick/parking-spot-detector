# utils.py
from ultralytics import YOLO
import os

def load_model(version="yolov8"):
    version_paths = {
        "yolov8": "./results/yolo_v8/result/weights/best.pt",
        "yolov9": "./results/yolo_v9/result/weights/best.pt", 
        "yolov10": "./results/yolo_v10/result/weights/best.pt",
        "yolov11": "./results/yolo_v11/result/weights/best.pt"
    }
    
    model_path = version_paths.get(version)
    if not model_path or not os.path.exists(model_path):
        raise ValueError(f"Modelo {version} não encontrado em {model_path}")

    model = YOLO(model_path)
    return model