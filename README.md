# Parking Spot Detector

Parking spot detection for real parking images using YOLO. This branch includes data processing, training scripts for multiple YOLO versions, video testing, and a small Flask API for image detection.

For the simplified YOLOv8 project using HotWheels cars in a simulated parking environment, see the [`hotwheels`](https://github.com/marcosschlick/parking-spot-detector/tree/hotwheels) branch.

## Setup

```bash
git clone https://github.com/marcosschlick/parking-spot-detector.git
cd parking-spot-detector
pip install -r requirements.txt
```

## Dataset

Download the parking spot dataset and place it at the project root:

```text
parking-spot-dataset/
```

Expected raw data layout:

```text
parking-spot-dataset/raw/images
parking-spot-dataset/raw/annotations
```

## Preprocess Data

Run the processing scripts in order:

```bash
python src/data_processing/resize_dataset.py
python src/data_processing/labelme_2_yolo.py
python src/data_processing/organize_dataset.py
```

The last command creates the YOLO dataset structure in `dataset/` and generates `dataset/data.yaml`.

## Train

Use one of the version-specific training scripts:

```bash
python src/scripts/train_model_v8.py
python src/scripts/train_model_v9.py
python src/scripts/train_model_v10.py
python src/scripts/train_model_v11.py
```

Each script uses `config.yaml` and saves results under a version-specific folder:

```text
results/yolo_v8/result/weights/best.pt
results/yolo_v9/result/weights/best.pt
results/yolo_v10/result/weights/best.pt
results/yolo_v11/result/weights/best.pt
```

## Test With Video

The default test script uses YOLOv8:

```bash
python src/scripts/test_latest_model.py
```

To test another version, change `MODEL_VERSION` at the top of `src/scripts/test_latest_model.py`.

## API

Start the API server:

```bash
python src/api/app.py
```

Test with the default YOLOv8 model:

```bash
curl -X POST -F "image=@images-api-test/image_01.png" http://localhost:5000/detect/image
```

Test a specific YOLO version:

```bash
curl -X POST -F "image=@images-api-test/image_01.png" "http://localhost:5000/detect/image?version=yolov11"
```

Supported versions are `yolov8`, `yolov9`, `yolov10`, and `yolov11`.

## Project Structure

```text
config.yaml
images-api-test/
LICENSE
parking-spot-dataset/
requirements.txt
src/
  api/
  data_processing/
  scripts/
```

## License

The source code in this project is licensed under the [MIT License](LICENSE).

Datasets, third-party dependencies, and pretrained YOLO models are subject to their respective licenses and terms of use.
