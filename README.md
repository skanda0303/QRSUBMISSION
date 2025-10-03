Multi-QR Code Recognition for Medicine Packs 💊

Overview

A Multi-QR Code Recognition System designed to detect and decode multiple QR codes from images of medicine packs. It extracts values, classifies them, and records bounding box positions in JSON format.

Key Features





Detect multiple QR codes in a single image



Extract QR code values and classify types



Provide bounding box coordinates



Export results in structured JSON format



Support for batch processing

Technology





Python 3.10+



OpenCV for image processing and QR code decoding



PyTorch / YOLOv8 (optional) for object detection



JSON for structured output

Project Structure

QRSUBMISSION/
├── README.md
├── requirements.txt
├── train.py
├── infer.py
├── evaluate.py
├── data/
│   └── demo_images/
├── outputs/
│   ├── submission_detection_1.json
│   └── submission_decoding_2.json
├── src/
│   ├── models/
│   ├── datasets/
│   └── utils.py

Installation

1. Clone the repository

git clone https://github.com/skanda0303/QRSUBMISSION.git
cd QRSUBMISSION

2. Install dependencies

pip install -r requirements.txt

3. Install YOLOv8 (optional)

pip install ultralytics

Usage

1. Prepare images

Place your medicine pack images into the data/demo_images/ directory.

2. Run detection and decoding

python infer.py --input data/demo_images/ --output outputs/results.json
