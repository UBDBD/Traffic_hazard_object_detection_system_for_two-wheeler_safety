import os
import shutil

source_folders = [
    '/content/drive/MyDrive/traffic_hazard/data_ctg/labels_맨홀',
    '/content/drive/MyDrive/traffic_hazard/data_ctg/labels_물통',
    '/content/drive/MyDrive/traffic_hazard/data_ctg/labels_쓰레기더미'
]

target_folder = '/content/drive/MyDrive/traffic_hazard/data_merge/lables'

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

for folder in source_folders:
    for filename in os.listdir(folder):
        source_file = os.path.join(folder, filename)
        target_file = os.path.join(target_folder, filename)

        if os.path.isfile(source_file):
            shutil.copy2(source_file, target_file)
            print(f'Copied {source_file} to {target_file}')

print('All files have been merged.')
