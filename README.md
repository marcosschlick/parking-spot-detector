# HotWheels Parking Spot Detector

Parking spot detection with YOLOv8 in a simulated HotWheels environment. This branch is intentionally simple: it includes data processing, YOLOv8 training, video testing, and realtime webcam detection.

For detection with real parking images and comparison between multiple YOLO versions, see the [`main`](https://github.com/marcosschlick/parking-spot-detector) branch.

## Setup

```bash
git clone https://github.com/marcosschlick/parking-spot-detector.git
cd parking-spot-detector
git checkout hotwheels
pip install -r requirements.txt
```

## Dataset

Download the HotWheels dataset and place it at the project root:

```text
hotwheels-dataset/
```

Expected raw data layout:

```text
hotwheels-dataset/raw/images
hotwheels-dataset/raw/annotations
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

Train the YOLOv8 model:

```bash
python src/scripts/train_model_v8.py
```

The trained model is saved at:

```text
results/yolo_v8/result/weights/best.pt
```

## Test With Video

```bash
python src/scripts/test_latest_model.py
```

## Realtime Detection

Run the webcam detector:

```bash
python src/app/realtime_parking_detector.py
```

The detector expects the trained YOLOv8 model at `results/yolo_v8/result/weights/best.pt`.

## Project Structure

```text
config.yaml
hotwheels-dataset/
LICENSE
requirements.txt
src/
  app/
  data_processing/
  scripts/
```

## License

The source code in this project is licensed under the [MIT License](LICENSE).

Datasets, third-party dependencies, and pretrained YOLO models are subject to their respective licenses and terms of use.
