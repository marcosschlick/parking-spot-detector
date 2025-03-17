import json
import os

# Caminhos atualizados
annotation_dir = "detector-vagas-hotwheels-dataset/processed/annotations_resized"
output_yolo_dir = "detector-vagas-hotwheels-dataset/processed/annotations_yolo"

# Cria o diretório de saída se não existir
os.makedirs(output_yolo_dir, exist_ok=True)

# Tamanho das imagens redimensionadas (use o mesmo valor do primeiro script)
new_size = (640, 853)  # ou (480, 640)

# Função para converter JSON (LabelMe) para YOLO
def convert_labelme_to_yolo(annotation_dir, output_yolo_dir):
    for annotation_name in os.listdir(annotation_dir):
        if not annotation_name.endswith(".json"):
            continue

        print(f"Convertendo {annotation_name}...")

        annotation_path = os.path.join(annotation_dir, annotation_name)

        # Verifica se o arquivo de anotação existe
        if not os.path.exists(annotation_path):
            print(f"Arquivo de anotação não encontrado: {annotation_name}. Pulando...")
            continue

        with open(annotation_path, "r") as f:
            annotation = json.load(f)

        # Verifica se há bounding boxes na anotação
        if not annotation["shapes"]:
            print(f"Nenhum bounding box encontrado em {annotation_name}. Pulando...")
            continue

        # Cria o arquivo YOLO
        yolo_file_path = os.path.join(output_yolo_dir, annotation_name.replace(".json", ".txt"))
        with open(yolo_file_path, "w") as f:
            for shape in annotation["shapes"]:
                label = shape["label"]
                points = shape["points"]

                # Converte pontos para formato YOLO (x_center, y_center, width, height)
                x_min = min(p[0] for p in points)
                x_max = max(p[0] for p in points)
                y_min = min(p[1] for p in points)
                y_max = max(p[1] for p in points)

                x_center = (x_min + x_max) / 2
                y_center = (y_min + y_max) / 2
                width = x_max - x_min
                height = y_max - y_min

                # Normaliza as coordenadas (0 a 1)
                x_center /= new_size[0]
                y_center /= new_size[1]
                width /= new_size[0]
                height /= new_size[1]

                # Valida as coordenadas normalizadas
                if not (0 <= x_center <= 1 and 0 <= y_center <= 1 and 0 <= width <= 1 and 0 <= height <= 1):
                    print(f"Coordenadas inválidas em {annotation_name}. Verifique as anotações.")
                    continue

                # Escreve no arquivo YOLO
                f.write(f"{0 if label == 'vaga_livre' else 1} {x_center} {y_center} {width} {height}\n")

# Executa a função
convert_labelme_to_yolo(annotation_dir, output_yolo_dir)
print("Conversão para YOLO concluída!")
