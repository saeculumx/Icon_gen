# SinsII Icon Generator

Hey everyone, just in case you are not happy with the tech tree or other icons in SinsII, here is a simple Python function I made to generate icons.

## Overview

This program allows you to generate new icons for SinsII by resizing your custom artwork to the required dimensions. You can see all the original artwork of SinsII in the "Source" folder. If you want to generate replacement icons for the game folder `...SinsII\textures`, follow the instructions below.

## Instructions

1. **Prepare Your Artwork**:
   - Ensure your custom artwork is sized in a 17:9 ratio.
   - Name your artwork files ending with `..._tooltip_picture200` (e.g., `my_custom_icon_tooltip_picture200.png`).

2. **Set Up Folders**:
   - Place all your replacement artwork in a folder named `Dir`.

3. **Run the Code**:
   - The code will then resize these images to various required dimensions and save them in the `output` folder.

4. **Replace Artwork**:
   - You are now able to overwrite SinsII\textures with resized icon

## Folders Structure

- `Source`: Contains the original artwork of SinsII.
- `Dir`: Place your replacement artwork here.
- `Output`: Generated icons will be saved here.

## Notes

- Ensure the `Dir` folder contains only the images you want to process, named correctly and sized in a 17:9 ratio if you dont want to see it in a strange shape in Sins.
- The output folder will contain subfolders for each original image, with resized versions of your replacement artwork.

Enjoy customizing your SinsII icons!
