from PIL.Image import Resampling
from tqdm import tqdm
from PIL import Image
import shutil
import os


def generate_images_for_all(base_folder, output_folder, sizes):
    """
    Generate images of different sizes for all images in the base folder.

    Args:
    - base_folder (str): Path to the folder containing base images.
    - output_folder (str): Path to the folder where output images will be saved.
    - sizes (dict): Dictionary with size names as keys and dimensions as values.

    Returns:
    - Dictionary with base image names as keys and lists of generated image paths as values.
    """
    generated_images_dict = {}

    # List all files in the base folder
    file_list = os.listdir(base_folder)
    progress = len(file_list)

    # Initialize the progress bar
    with tqdm(total=progress, desc="Processing images") as pbar:
        for base_image_name in file_list:
            base_name = base_image_name.split('.')[0]

            # Remove the 'tooltip_picture200' suffix if it exists
            if base_name.endswith('_tooltip_picture200'):
                base_name = base_name[:-len('_tooltip_picture200')]

            base_image_path = os.path.join(base_folder, base_image_name)

            if os.path.isfile(base_image_path):
                subfolder_path = os.path.join(output_folder, base_name)

                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)

                generated_images = []

                for suffix, size in sizes.items():
                    base_image = Image.open(base_image_path)

                    resized_image = base_image.resize(size, Resampling.LANCZOS)

                    output_path = os.path.join(subfolder_path, f"{base_name}_{suffix}.png")

                    resized_image.save(output_path)

                    generated_images.append(output_path)

                generated_images_dict[base_image_name] = generated_images

            # Update the progress bar
            pbar.update(1)

    return generated_images_dict


def copy_specific_images(source_folder, target_folder, keyword):
    """
    Copy all images containing a specific keyword in their filename from the source folder to the target folder.

    Args:
    - source_folder (str): Path to the folder containing the images to be copied.
    - target_folder (str): Path to the folder where the images will be copied.
    - keyword (str): Keyword to search for in the filenames.

    Returns:
    - List of paths to the copied images.
    """
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    copied_images = []

    for file_name in os.listdir(source_folder):
        if keyword in file_name:
            source_path = os.path.join(source_folder, file_name)
            target_path = os.path.join(target_folder, file_name)
            shutil.copy2(source_path, target_path)
            copied_images.append(target_path)

    return copied_images


source_folder = "C:/Program Files/Epic Games/SinsII/textures"
target_folder = "source"
keyword = "picture200"

sizes = {
    "tooltip_picture200": (918, 432),
    "hud_icon": (85, 40),
    "hud_icon150": (128, 60),
    "hud_icon200": (170, 80),
    "tooltip_picture": (459, 216),
    "tooltip_picture150": (689, 324)
}

# copied_images = copy_specific_images(source_folder, target_folder, keyword)

base_folder = "Dir"
output_folder = "output"

generated_images = generate_images_for_all(base_folder, output_folder, sizes)
