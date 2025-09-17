from flask import Flask, jsonify, request
import cv2
import numpy as np
from utils import load_model

app = Flask(__name__)

@app.route('/', methods=['GET'])
def status():
    return jsonify({"status": "ok"})

@app.route('/detect/image', methods=['POST'])
def detect_image():
    model = load_model()

    # Check if an image was received
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    # Read the image
    file = request.files['image']
    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Perform detection
    results = model(img)
    
    # Process results
    detections = []
    for result in results:
        available = 0
        occupied = 0
        for box in result.boxes:
            class_name = model.names[int(box.cls[0])]
            confidence = float(box.conf[0])
            
            if class_name == 'available':
                available += 1
            else:
                occupied += 1
                
            detections.append({
                "class": class_name,
                "confidence": confidence
            })
    
    response = {
        "summary": {
            "total_spaces": available + occupied,
            "available": available,
            "occupied": occupied
        },
        "detections": detections
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)