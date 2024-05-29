<h1 align="center">Poker Hand Detection with YOLOv8 through webcam</h1>

<p align="center">
  <img src="https://github.com/mrkrisgee/poker_hand_detection/blob/main/gifs/poker_hand_example.gif" alt="Webcam Feed">
</p>

## Overview

This repository contains code for training a large dataset of playing cards with YOLOv8, creating a poker hand detection system with python and then using the webcam live feed to make real-time predictions and identifying what type of hand someone has.

## Usage

**Note:** This step can be skipped and the provided model in the [`model/`](https://github.com/mrkrisgee/poker_hand_detection/tree/main/model) directory can be used instead.

## 1. Training the Model

### Download the Playing Cards Image Dataset

Download the dataset from the following link:

```
https://universe.roboflow.com/augmented-startups/playing-cards-ow27d/dataset/4/download/yolov8
```

### Organize Dataset in Google Drive

Add the dataset to your Google Drive with the following hierarchy:

<img src="https://github.com/mrkrisgee/poker_hand_detection/blob/main/extras/gDrive_hierarchy.png" width="1346/6" height="794/6">

### Train the Model

Download and run the training notebook:

```
https://github.com/mrkrisgee/poker_hand_detection/tree/main/train
```

### Retrieve and Download the Best Model

```
This will be saved in: `/runs/detect/train/weights/best.pt`
```

## 2. Making Real-time Predictions on your Webcam Feed

### Prerequisites

Ensure you have [Anaconda](https://www.anaconda.com/) installed on your system. Anaconda simplifies package management and deployment.

### Create a Virtual Environment

Create and activate a new conda environment by running the following commands in your terminal:

```
conda create -n yolov8
conda activate yolov8
```

### Clone the repository

Clone this repository to your local machine and navigate into the project directory:

```
git clone https://github.com/mrkrisgee/poker_hand_detection.git
cd poker_hand_detection
```

### Move the Trained Model and Rename it

Move the `best.pt` model to the `/poker_hand_detection/model/ directory` and rename it to `playingCards.pt`.

### Install Necessary Packages

Install the required Python packages using pip:

```
pip install -r requirements.txt
```

### Download CUDA Toolkit

If you have an NVIDIA GPU and want to utilize CUDA for acceleration, download and install the CUDA toolkit from the [NVIDIA CUDA Downloads](https://developer.nvidia.com/cuda-downloads) page.

```
https://developer.nvidia.com/cuda-downloads
```

### Run the Scripts

To execute the poker_hand_detection script, run:

```
poker_hand_detector.py
```

## References

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics): YOLOv8 is a real-time object detection model developed by Ultralytics.
- [Alex Bewley](https://github.com/abewley/sort): For providing the SORT (Simple Online and Realtime Tracking) algorithm used for object tracking.
- [Murtaza Hassan](https://github.com/murtazahassan): For his comprehensive Object Detection 101 course
