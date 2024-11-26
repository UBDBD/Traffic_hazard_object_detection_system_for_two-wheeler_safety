import json
import os
import chardet

json_dir = 'C:/Users/sehyu/Desktop/data/valid/json/쓰레기더미'
label_dir = 'E:/yolo_data/labels/labels_쓰레기더미'

class_map = {
    "16.쓰레기(쓰레기더미)": 2
}

if not os.path.exists(label_dir):
    os.makedirs(label_dir)

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

for json_file in os.listdir(json_dir):
    if json_file.endswith(".json"):
        json_path = os.path.join(json_dir, json_file)
        
        encoding = detect_encoding(json_path)
        if encoding is None:
            print(f"Cannot detect encoding for {json_file}")
            continue
        
        try:
            with open(json_path, 'r', encoding=encoding) as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading {json_file}: {e}")
            continue
        
        image_info = data['images']
        image_width = image_info['width']
        image_height = image_info['height']
        
        annotations = data['annotation']
        
        json_filename_without_ext = os.path.splitext(json_file)[0]
        label_file = os.path.join(label_dir, f"{json_filename_without_ext}.txt")
        
        with open(label_file, 'w') as f:
            for annotation in annotations:
                label = annotation['label']
                if label not in class_map:
                    continue
                class_id = class_map[label]
                
                bbox = annotation['bbox']
                x_min, y_min, box_width, box_height = bbox
                
                x_center = (x_min + box_width / 2) / image_width
                y_center = (y_min + box_height / 2) / image_height
                box_width /= image_width
                box_height /= image_height
                
                f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")

        print(f"Processed {json_file} with encoding {encoding} -> {label_file}")

print('finish')
