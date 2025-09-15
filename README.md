# Parking Spot Detector

Parking space detection using YOLOv8. Includes data processing, training, and real-time inference.

---

## How to Use

### 1. Clone and Setup

```bash
git clone https://github.com/marcosschlick/parking-spot-detector.git
cd parking-spot-detector
pip install -r requirements.txt
```

### 2. Download Dataset

- Download the dataset [here](https://drive.google.com/drive/folders/1JycO-is7-qS4FMPF5KWqwNeS56z7pxHV?usp=drive_link)
- Place the `parking-spot-dataset` folder at the root of the project

### 3. Process Data

```bash
python src/data_processing/resize_dataset.py
python src/data_processing/labelme_2_yolo.py
python src/data_processing/organize_dataset.py
```

### 4. Train Model

```bash
yolo train data=config.yaml model=yolov8n.pt epochs=30 imgsz=640 project=./results name="result_$(date +'%Y-%m-%d_%H:%M:%S')"
```

### 5. Test

**Automatic testing with video (uses latest model):**

```bash
python src/scripts/test_latest_model.py
```

**Manual testing with video (choose model manually):**

```bash
yolo predict model={model_path} source=./parking-spot-dataset/test/videos/test_parking_01.mp4 show=True save=True imgsz=1280 line_width=1 project=./predictions
```

Replace `{model_path}` with the path to your desired model (e.g., `./results/result_2025-09-20_12:12:12/weights/best.pt`).

---

## Project Structure

```
├── config.yaml
├── dataset
├── parking-spot-dataset
├── requirements.txt
├── results
└── src
    ├── data_processing
    │   ├── labelme_2_yolo.py
    │   ├── organize_dataset.py
    │   └── resize_dataset.py
    └── scripts
        ├── check_dependencies.py
        └── test_latest_model.py
```
