# Detector de Vagas HotWheels

Detecção de vagas de estacionamento com YOLOv8 em ambiente simulado (pistas de papel + Hot Wheels). Inclui processamento de dados, treinamento e inferência em tempo real.

---

## Como Usar

### 1. Clonar e Configurar
```bash
git clone https://github.com/marcosschlick/detector-vagas-hotwheels.git
cd detector-vagas-hotwheels
pip install -r requirements.txt
```

### 2. Baixar Dataset
- Baixe o dataset [aqui](https://drive.google.com/drive/folders/14O0ukMquMIgOXa-5Hx-iz1jMh8zIkxNO?usp=drive_link)
- Coloque `detector-vagas-hotwheels-dataset` na raiz do projeto

### 3. Processar Dados
```bash
python src/data_processing/resize_dataset.py
python src/data_processing/labelme_2_yolo.py
python src/data_processing/organize_dataset.py
```

### 4. Treinar Modelo
```bash
yolo train data=config.yaml model=yolov8n.pt epochs=50 imgsz=640
```

### 5. Testar
**Com vídeo:**
```bash
yolo predict model=runs/detect/train/weights/best.pt source=detector-vagas-hotwheels-dataset/test/videos/test_hotwheels_01.mp4 show=True
```

**Com câmera em tempo real:**
```bash
python src/app/realtime_parking_detector.py
```

---

## Estrutura do Projeto
```
├── config.yaml
├── dataset
├── detector-vagas-hotwheels-dataset
├── requirements.txt
├── runs
└── src
    ├── app
    │   └── realtime_parking_detector.py
    ├── data_processing
    │   ├── labelme_2_yolo.py
    │   ├── organize_dataset.py
    │   └── resize_dataset.py
    └── test.py
```

---

## Licença
MIT - [LICENSE](LICENSE)
