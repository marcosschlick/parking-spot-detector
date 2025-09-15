import os
import subprocess

# Find the most recent directory in the results folder
results_dir = "./results"  
all_subdirs = [os.path.join(results_dir, d) for d in os.listdir(results_dir) 
               if os.path.isdir(os.path.join(results_dir, d)) and d.startswith("result_")]
latest_dir = max(all_subdirs, key=os.path.getmtime)

# Build the path to the best model
model_path = os.path.join(latest_dir, "weights", "best.pt")

# Verify if the model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found: {model_path}")

# Execute the prediction command
video_source = "./parking-spot-dataset/test/videos/test_parking_01.mp4"
command = f"yolo predict model={model_path} source={video_source} show=True save=True line_width=1 project=./predictions"

subprocess.run(command, shell=True, check=True)