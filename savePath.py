import os
import json

image_base_dir = './example_cropped'
label_base_dir = './labels'
noun_base_dir = './nouns'

path_list = []

# Function to recursively find image files in subdirectories
def find_image_files(base_dir):
    image_files = []
    for root, _, files in os.walk(base_dir):
        files.sort()    
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                image_files.append(os.path.join(root, file))
    return image_files

# Function to generate the corresponding paths for each image
def generate_data(image_path):
    # Extract image_name without extension and folder name
    image_name = os.path.splitext(os.path.basename(image_path))[0]
     
    # Construct the corresponding paths for label and noun files
    label_subdir = os.path.relpath(os.path.dirname(image_path), image_base_dir)
    image_type = label_subdir
    label_path = os.path.join(label_base_dir, label_subdir, f'{image_name}_labels.json')
    noun_path = os.path.join(noun_base_dir, label_subdir, f'{image_name}.json')

    image_data = {
        "image_name": image_name,
        "image_type": image_type,
        "image_path": image_path,
        "label_path": label_path,
        "noun_path": noun_path
    }

    return image_data

image_files = find_image_files(image_base_dir)

print(f"Found {len(image_files)} image files")

for image_file in image_files:
    image_data = generate_data(image_file)
    path_list.append(image_data)

# Define the path where you want to save the JSON file
output_json_path = 'paths_example.json'

# Write the list to a JSON file
with open(output_json_path, 'w') as json_file:
    json.dump(path_list, json_file, indent=2)

print(f"JSON file has been written to {output_json_path}")
