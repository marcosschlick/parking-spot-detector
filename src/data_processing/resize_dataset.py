import cv2
import os
import json

INPUT_IMAGE_DIR = "parking-spot-dataset/raw/images"
OUTPUT_IMAGE_DIR = "parking-spot-dataset/processed/images_resized" 

INPUT_ANNOTATION_DIR = "parking-spot-dataset/raw/annotations"  
OUTPUT_ANNOTATION_DIR = "parking-spot-dataset/processed/annotations_resized" 

TARGET_SIZE = 640
PADDING_COLOR = (0, 0, 0) 

os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)
os.makedirs(OUTPUT_ANNOTATION_DIR, exist_ok=True)

def process_image(image_path):
    """load and resize image with aspect ratio preservation"""
    image = cv2.imread(image_path)
    if image is None:
        return None, None
    
    h, w = image.shape[:2]
    
    # calculate scaling factors
    scale = min(TARGET_SIZE / w, TARGET_SIZE / h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    
    # resize image
    resized = cv2.resize(image, (new_w, new_h))
    
    # apply padding
    pad_x = (TARGET_SIZE - new_w) // 2
    pad_y = (TARGET_SIZE - new_h) // 2
    padded = cv2.copyMakeBorder(
        resized, pad_y, pad_y, pad_x, pad_x, 
        cv2.BORDER_CONSTANT, value=PADDING_COLOR
    )
    
    return padded, (scale, pad_x, pad_y)

def process_annotation(annotation_path, scale_factors):
    """adjust annotations with scaling and padding"""
    with open(annotation_path, 'r') as f:
        data = json.load(f)
    
    scale, pad_x, pad_y = scale_factors
    
    for shape in data['shapes']:
        for point in shape['points']:
            # apply scaling
            point[0] = point[0] * scale
            point[1] = point[1] * scale
            
            # apply padding
            point[0] += pad_x
            point[1] += pad_y
    
    return data

def main():
    """process all images and annotations"""
    for img_name in os.listdir(INPUT_IMAGE_DIR):
        if not img_name.lower().endswith('.png'):
            continue
            
        img_path = os.path.join(INPUT_IMAGE_DIR, img_name)
        img, scale_factors = process_image(img_path)
        
        if img is None:
            print(f"skipping invalid image: {img_name}")
            continue
        
        # save processed image
        out_img_path = os.path.join(OUTPUT_IMAGE_DIR, img_name)
        cv2.imwrite(out_img_path, img)
        
        # process corresponding annotation
        ann_name = img_name.replace('.png', '.json')
        ann_path = os.path.join(INPUT_ANNOTATION_DIR, ann_name)
        
        if not os.path.exists(ann_path):
            print(f"annotation missing for {img_name}")
            continue
            
        updated_ann = process_annotation(ann_path, scale_factors)
        
        # save updated annotation
        out_ann_path = os.path.join(OUTPUT_ANNOTATION_DIR, ann_name)
        with open(out_ann_path, 'w') as f:
            json.dump(updated_ann, f)

    print("image processing completed")

if __name__ == "__main__":
    main()