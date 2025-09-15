import json
import os

ANNOTATION_DIR = "hotwheels-dataset/processed/annotations_resized"
OUTPUT_DIR = "hotwheels-dataset/processed/annotations_yolo"
IMG_SIZE = 640  

os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_annotation():
    """convert LabelMe annotations to YOLO format"""
    for ann_file in os.listdir(ANNOTATION_DIR):
        if not ann_file.endswith(".json"):
            continue
            
        ann_path = os.path.join(ANNOTATION_DIR, ann_file)
        
        try:
            with open(ann_path) as f:
                data = json.load(f)
        except:
            continue
            
        if not data.get("shapes"):
            continue
            
        # prepare output file
        out_file = os.path.join(OUTPUT_DIR, ann_file.replace(".json", ".txt"))
        
        with open(out_file, "w") as f:
            for shape in data["shapes"]:
                label = shape["label"]
                points = shape["points"]
                
                # calculate bounding box
                xs = [p[0] for p in points]
                ys = [p[1] for p in points]
                x_min, x_max = min(xs), max(xs)
                y_min, y_max = min(ys), max(ys)
                
                # convert to YOLO format
                x_center = (x_min + x_max) / 2
                y_center = (y_min + y_max) / 2
                width = x_max - x_min
                height = y_max - y_min
                
                # normalize
                x_center /= IMG_SIZE
                y_center /= IMG_SIZE
                width /= IMG_SIZE
                height /= IMG_SIZE
                
                # validate and write
                if all(0 <= val <= 1 for val in (x_center, y_center, width, height)):
                    class_id = 0 if label == "available" else 1
                    f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

if __name__ == "__main__":
    convert_annotation()
    print("conversion complete")