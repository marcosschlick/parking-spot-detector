from ultralytics import YOLO
import os

def load_model():
    # Find the most recent directory in the results folder
    results_dir = "./results"  
    all_subdirs = [os.path.join(results_dir, d) for d in os.listdir(results_dir) 
                    if os.path.isdir(os.path.join(results_dir, d)) and d.startswith("result_")]
    latest_dir = max(all_subdirs, key=os.path.getmtime)

    # Build the path to the best model
    model_path = os.path.join(latest_dir, "weights", "best.pt")

    # Load best model
    model = YOLO(model_path)
    return model