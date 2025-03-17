import os
import random
import shutil
from sklearn.model_selection import train_test_split

# Caminhos
images_resized_dir = "detector-vagas-hotwheels-dataset/processed/images_resized"  # Imagens redimensionadas
annotations_yolo_dir = "detector-vagas-hotwheels-dataset/processed/annotations_yolo"  # Anotações YOLO
output_dir = "dataset"  # Pasta final para o YOLO

# Proporção de divisão (80% treino, 20% validação)
train_ratio = 0.8

# Cria as pastas de saída
os.makedirs(os.path.join(output_dir, "images/train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "images/val"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels/train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels/val"), exist_ok=True)

# Lista de arquivos de imagens
image_files = [f for f in os.listdir(images_resized_dir) if f.endswith(".jpg")]

# Divide os arquivos em treino e validação
train_files, val_files = train_test_split(image_files, train_size=train_ratio, random_state=42)

# Função para mover arquivos
def move_files(files, source_dir, target_dir):
    for file in files:
        shutil.move(os.path.join(source_dir, file), os.path.join(target_dir, file))

# Move as imagens de treino
move_files(train_files, images_resized_dir, os.path.join(output_dir, "images/train"))

# Move as imagens de validação
move_files(val_files, images_resized_dir, os.path.join(output_dir, "images/val"))

# Move as anotações de treino
move_files([f.replace(".jpg", ".txt") for f in train_files], annotations_yolo_dir, os.path.join(output_dir, "labels/train"))

# Move as anotações de validação
move_files([f.replace(".jpg", ".txt") for f in val_files], annotations_yolo_dir, os.path.join(output_dir, "labels/val"))

print("Organização do dataset concluída!")
