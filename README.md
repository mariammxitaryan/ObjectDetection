# Instance Segmentation CLI

A simple, user-friendly Python command-line tool for instance segmentation using PixelLib and TensorFlow.

## Features

- **Interactive CLI menu** for:
  - Specifying model, input file, and output file paths
  - Selecting target COCO classes to segment
  - Choosing actions: segment only, count objects, extract objects, or save masks
- **Modular functions** for processing both images and videos
- **Default model path** can be overridden at runtime
- **Clear error handling** with informative messages

## Requirements

- Python 3.6+
- [TensorFlow](https://www.tensorflow.org/) (tested with TF 2.x and TF 1 compatibility)
- [PixelLib](https://github.com/ayoolaolafenwa/PixelLib)

## Installation

1. Clone this repository:

2. Install dependencies:
   ```bash
   pip install tensorflow pixellib
   ```

3. Download the COCO Mask R-CNN model weights (`mask_rcnn_coco.h5`):
   ```bash
   wget https://github.com/ayoolaolafenwa/PixelLib/releases/download/Mask_RCNN/mask_rcnn_coco.h5
   ```

4. Place `mask_rcnn_coco.h5` in the project root (or specify its location at runtime).

## Usage

Run the script from your terminal:

```bash
python segment_cli.py
```

You will be prompted to:

1. **Model path** (press Enter to use default `./mask_rcnn_coco.h5`)
2. **Input file** (image or video)
3. **Output path** (default: `output.jpg` or `output_video.mp4`)
4. **Target classes** (comma-separated, default: `person`)
5. **Action**:
   - `1` Segment and save
   - `2` Count objects
   - `3` Extract objects
   - `4` Show/save masks

Example:

```bash
Enter path to Mask R-CNN model (.h5) [default: ./mask_rcnn_coco.h5]:
Enter path to the input image or video: my_photo.jpg
Enter output path [default: output.jpg]: segmented.jpg
Enter target classes separated by commas (e.g. person,car) [default: person]: person,car
Select action on segmented objects:
  1) Just segment and save
  2) Count each class and print totals
  3) Extract each object to its own file
  4) Show/save only masks
Enter 1, 2, 3, or 4 [default: 1]: 1
```

The script will process `my_photo.jpg`, segment people and cars, draw bounding boxes (and masks if selected), and save the result to `segmented.jpg`.

## Code Structure

- **`setup_eager_execution()`**: Enables TF eager execution for compatibility
- **`load_segmentation_model(path)`**: Loads Mask R-CNN model
- **`segment_image(...)` / `segment_video(...)`**: Core segmentation with selected action
- **`get_user_choices()`**: Interactive prompts for all parameters
- **`main()`**: Orchestrates setup, user input, and segmentation


