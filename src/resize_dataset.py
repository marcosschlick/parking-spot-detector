import cv2
import os
import json

# Caminhos atualizados
image_dir = "detector-vagas-hotwheels-dataset/raw/images"  # Imagens brutas
annotation_dir = "detector-vagas-hotwheels-dataset/raw/annotations"  # Anotações brutas
output_image_dir = "detector-vagas-hotwheels-dataset/processed/images_resized"  # Imagens redimensionadas
output_annotation_dir = "detector-vagas-hotwheels-dataset/processed/annotations_resized"  # Anotações redimensionadas

# Cria os diretórios de saída se não existirem
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_annotation_dir, exist_ok=True)

# Novo tamanho (largura, altura)
new_size = (640, 853)  # ou (480, 640)

# Função para redimensionar imagens e ajustar bounding boxes
def resize_images_and_annotations(image_dir, annotation_dir, output_image_dir, output_annotation_dir, new_size):
    for image_name in os.listdir(image_dir):
        if not image_name.endswith(".jpg"):
            continue

        print(f"Processando {image_name}...")

        # Carrega a imagem
        image_path = os.path.join(image_dir, image_name)
        image = cv2.imread(image_path)
        if image is None:
            print(f"Erro ao carregar {image_name}. Pulando...")
            continue

        original_height, original_width = image.shape[:2]

        # Redimensiona a imagem
        resized_image = cv2.resize(image, new_size)
        resized_image_path = os.path.join(output_image_dir, image_name)
        cv2.imwrite(resized_image_path, resized_image)

        # Ajusta os rótulos (bounding boxes)
        annotation_name = image_name.replace(".jpg", ".json")
        annotation_path = os.path.join(annotation_dir, annotation_name)

        if not os.path.exists(annotation_path):
            print(f"Arquivo de anotação não encontrado para {image_name}. Pulando...")
            continue

        with open(annotation_path, "r") as f:
            annotation = json.load(f)

        if not annotation["shapes"]:
            print(f"Nenhum bounding box encontrado para {image_name}. Pulando...")
            continue

        # Ajusta as coordenadas dos bounding boxes
        for shape in annotation["shapes"]:
            points = shape["points"]
            for point in points:
                point[0] = point[0] * (new_size[0] / original_width)  # Ajusta X
                point[1] = point[1] * (new_size[1] / original_height)  # Ajusta Y

        # Salva o novo arquivo de anotação
        resized_annotation_path = os.path.join(output_annotation_dir, annotation_name)
        with open(resized_annotation_path, "w") as f:
            json.dump(annotation, f)

# Executa a função
resize_images_and_annotations(image_dir, annotation_dir, output_image_dir, output_annotation_dir, new_size)
print("Redimensionamento concluído!")
