import os
import shutil
from sklearn.model_selection import train_test_split

IMAGE_DIR = "parking-spot-dataset/processed/images_resized"
ANNOTATION_DIR = "parking-spot-dataset/processed/annotations_yolo"
OUTPUT_DIR = "dataset"

# create output structure
os.makedirs(f"{OUTPUT_DIR}/images/train", exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/images/val", exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/labels/train", exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/labels/val", exist_ok=True)

# get image files
image_files = [f for f in os.listdir(IMAGE_DIR) if f.endswith(".png")]

# split dataset (80% train, 20% validation)
train_files, val_files = train_test_split(image_files, test_size=0.2, random_state=42)

# move files to organized structure
for files, split in [(train_files, "train"), (val_files, "val")]:
    # move images
    for img in files:
        src = os.path.join(IMAGE_DIR, img)
        dst = os.path.join(OUTPUT_DIR, "images", split, img)
        shutil.move(src, dst)
    
    # move corresponding annotations
    for img in files:
        ann = img.replace(".png", ".txt")
        src = os.path.join(ANNOTATION_DIR, ann)
        dst = os.path.join(OUTPUT_DIR, "labels", split, ann)
        shutil.move(src, dst)

print("dataset organized successfully")