# Detector de Vagas para HotWheels

Este projeto utiliza o YOLOv8 para detectar vagas de estacionamento em um ambiente simulado, onde pistas de papel representam o cenário e carrinhos Hot Wheels atuam como veículos. Inclui scripts completos para processamento de dados, treinamento do modelo e inferência em vídeos, oferecendo uma solução prática e educativa para sistemas de detecção em pequena escala.

---

## Como Usar

### 1. Clonar o Repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/marcosschlick/detector-vagas-hotwheels.git
cd detector-vagas-hotwheels
```

---

### 2. Baixar o Dataset

1. Acesse o link do Google Drive: [Detector Vagas Hot Wheels Dataset](https://drive.google.com/drive/folders/14O0ukMquMIgOXa-5Hx-iz1jMh8zIkxNO?usp=drive_link).
2. Baixe a pasta `detector-vagas-hotwheels-dataset`.
3. Coloque a pasta baixada na **raiz do projeto**.

---

### 3. Instalar Dependências

Instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

---

### 4. Processar os Dados

Execute os scripts na seguinte ordem:

1. **Redimensionar imagens e anotações**:
   ```bash
   python src/resize_dataset.py
   ```

2. **Converter anotações para o formato YOLO**:
   ```bash
   python src/labelme_2_yolo.py
   ```

3. **Organizar dataset para treino e validação**:
   ```bash
   python src/organize_dataset.py
   ```

---

### 5. Treinar o Modelo

Treine o modelo YOLOv8 com o dataset processado:

```bash
yolo train data=config.yaml model=yolov8n.pt epochs=50 imgsz=640
```

---

### 6. Testar com Vídeo

Faça inferências em um vídeo de teste:

```bash
yolo predict model=runs/detect/train/weights/best.pt source=detector-vagas-hotwheels-dataset/test/videos/test_hotwheels_01.mp4 show=True
```

---

Resultados

Os resultados do treinamento e inferência podem ser acessados no link abaixo:
[Resultados do Projeto](https://drive.google.com/drive/folders/1MPpq3anPEHgDgY-Yl-RTG29htYtGPxIW?usp=drive_link)

---

## Estrutura do Projeto

```
detector-vagas-hotwheels/
├── detector-vagas-hotwheels-dataset/  # Dataset baixado do Google Drive
├── dataset/                                # Dataset processado (gerado automaticamente)
├── src/                                    # Scripts do projeto
│   ├── resize_dataset.py                   # Redimensiona imagens e anotações
│   ├── labelme_2_yolo.py                   # Converte anotações para o formato YOLO
│   └── organize_dataset.py                 # Organiza dataset para treino e validação
├── runs/                                   # Resultados de treinamento e inferência (gerado automaticamente)
├── config.yaml                             # Configuração do YOLO
├── requirements.txt                        # Dependências do projeto
└── README.md                               # Documentação do projeto
```

---

## Requisitos

- Python 3.13.2.
- Bibliotecas listadas no `requirements.txt`.

---

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

