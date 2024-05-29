<h1 align="center">Real-time Poker Hand Detection with YOLOv8 via Webcam</h1>

<p align="center">
  <img src="https://github.com/mrkrisgee/poker_hand_detection/blob/main/gifs/poker_hand_example.gif" alt="Webcam Feed">
</p>

## Table of Contents
- Overview
- Features
- Usage
  - Training the Model
      - Download the Playing Cards Image Dataset
      - Organize Dataset in Google Drive
      - Train the Model
      - Retrieve and Download the Best Model
  - Making Real-time Predictions
      - Prerequisites
      - Create a Virtual Environment
      - Clone the Repository
      - Move and Rename the Trained Model
      - Install Necessary Packages
      - Download CUDA Toolkit
      - Run the Script
- References    

## Overview

This repository contains code for training a YOLOv8 model on a large dataset of playing cards to create a poker hand detection system using Python. It includes a setup for using a webcam live feed to make real-time predictions and identify poker hands.

## Features

- Real-time detection of poker hands using a webcam.
- Pre-trained YOLOv8 model for quick setup.
- Easy-to-follow training process for custom datasets.
- Integration with CUDA for accelerated performance.

## Usage

You can skip the training steps and use the pre-trained model provided in the [model/](https://github.com/mrkrisgee/poker_hand_detection/tree/main/model) directory.

## 1. Training the Model

### Download the Playing Cards Image Dataset

Download the dataset from the following link:

```
https://universe.roboflow.com/augmented-startups/playing-cards-ow27d/dataset/4/download/yolov8
```

### Organize Dataset in Google Drive

Add the dataset to your Google Drive with the following hierarchy:

<img src="https://github.com/mrkrisgee/poker_hand_detection/blob/main/extras/gDrive_hierarchy.png" width="673">

### Train the Model

Download and run the training notebook:

```
https://github.com/mrkrisgee/poker_hand_detection/tree/main/train
```

### Retrieve and Download the Best Model

Once training is complete, download the "best" model from:

```
/runs/detect/train/weights/best.pt
```

## 2. Making Real-time Predictions

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

Move the best.pt model to the /poker_hand_detection/model/ directory and rename it to playingCards.pt.

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

### Run the Script

To execute the poker_hand_detection script, run:

```
poker_hand_detector.py
```

## References

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics): YOLOv8 is a real-time object detection model developed by Ultralytics.
- [Alex Bewley](https://github.com/abewley/sort): For providing the SORT (Simple Online and Realtime Tracking) algorithm used for object tracking.
- [Murtaza Hassan](https://github.com/murtazahassan): For his comprehensive Object Detection 101 course
