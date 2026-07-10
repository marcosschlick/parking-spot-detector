import os
import subprocess

model_path = "./results/yolo_v8/result/weights/best.pt"

# Verify if the model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found: {model_path}")

# Execute the prediction command
video_source = "./hotwheels-dataset/test/videos/test_hotwheels_01.mp4"
command = f"yolo predict model={model_path} source={video_source} show=True save=True line_width=1 project=./predictions"

subprocess.run(command, shell=True, check=True)
