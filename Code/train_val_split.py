import splitfolders

input_folder = "/content/drive/MyDrive/valid"
output_folder = "/content/drive/MyDrive/valid_split"

splitfolders.ratio(input_folder, output=output_folder, seed=1337, ratio=(0.8, 0.2), group_prefix=None)
