# README for VBA Image Captioning and Resizing Macro

## Description

This VBA (Visual Basic for Applications) macro is designed to automate the process of inserting, captioning, and resizing images within a Microsoft Word document. The macro enables users to efficiently place multiple images with captions on a page, formatted to specified dimensions and arranged in a grid layout.

## Features

- **Image Selection:** Utilizes a file dialog that allows for multiple image selections.
- **Automatic Captioning:** Generates captions based on the image file names and positions them below the respective images.
- **Consistent Sizing:** Resizes all images to predetermined dimensions.
- **Grid Layout:** Arranges images in a grid format with a specified number of images per page.
- **Page Management:** Automatically inserts page breaks after a certain number of images and continues the process on a new page.
- **Custom Spacing:** Calculates and maintains consistent spacing between images based on page dimensions and margins.

## How It Works

1. **Image Per Page:** The macro is set to place a default number of images per page, which can be adjusted as needed.
2. **Image and Caption Sizing:** It defines the desired dimensions for the images and the captions based on the given measurements.
3. **Page Layout:** Determines the page setup including page width, height, and margins.
4. **Image Insertion and Resizing:** Inserts each selected image into the document, resizes it, and places it in the correct grid position.
5. **Caption Box Creation:** Generates a text box for each image caption, positions it below the image, and ensures it has no fill or line color for a clean appearance.
6. **Page Break Insertion:** Inserts a page break when the image count reaches the per-page limit and resets the count for the next page.

## Note

Please note I completed this before my programming journey began. I had a lot of help but I am proud of this work nonetheless.
