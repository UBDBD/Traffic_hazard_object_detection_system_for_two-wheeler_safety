import yaml

data = {'train': '/content/drive/MyDrive/traffic_hazard/data_split/train/images',
        'val': '/content/drive/MyDrive/traffic_hazard/data_split/val/images',
        'name': ['manhole','bucket','trash'],
        'nc': 3}

with open('/content/drive/MyDrive/traffic_hazard/traffic_hazard.yaml', 'w') as f:
  yaml.dump(data, f)

with open('/content/drive/MyDrive/traffic_hazard/traffic_hazard.yaml', 'r') as f:
  traffic_hazard_yaml = yaml.safe_load(f)
  display(traffic_hazard_yaml)