import os
import subprocess

MODEL_VERSION = "yolov8"

MODEL_PATHS = {
    "yolov8": "./results/yolo_v8/result/weights/best.pt",
    "yolov9": "./results/yolo_v9/result/weights/best.pt",
    "yolov10": "./results/yolo_v10/result/weights/best.pt",
    "yolov11": "./results/yolo_v11/result/weights/best.pt",
}

model_path = MODEL_PATHS.get(MODEL_VERSION)
if not model_path:
    supported_versions = ", ".join(MODEL_PATHS)
    raise ValueError(f"Unsupported model version '{MODEL_VERSION}'. Use one of: {supported_versions}")

# Verify if the model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found: {model_path}")

# Execute the prediction command
video_source = "./parking-spot-dataset/test/videos/test_parking_01.mp4"
command = f"yolo predict model={model_path} source={video_source} show=True save=True line_width=1 project=./predictions"

subprocess.run(command, shell=True, check=True)
