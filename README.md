Multi-QR Code Recognition for Medicine Packs
Project Overview

This project is a Multi-QR Code Recognition System designed to detect and decode multiple QR codes from images of medicine packs. Many medicine packs contain multiple QR codes, such as codes for manufacturers, batch numbers, distributors, and regulators. This system accurately detects all QR codes in a single image and extracts their values and positions.

Features

Detect multiple QR codes in a single image.

Extract QR code values and types.

Provide bounding box coordinates for each QR code.

Export results in structured JSON format.

Can be extended for batch processing of multiple medicine images.

Demo

Example output for an image:

{
"image_id": "img220.jpg",
"qrs": [
{
"bbox": [927.21, 249.28, 1059.42, 376.46],
"value": "5a0RlO0E",
"type": "Other"
},
{
"bbox": [1574.55, 171.54, 1705.96, 298.87],
"value": "5a0RlO0G",
"type": "Other"
}
]
}

Technology Stack

Python 3.10+

OpenCV for image preprocessing and QR code detection

PyTorch / YOLOv8 for object detection of QR codes (optional for advanced models)

JSON for storing and exporting detection results

Installation

Clone the repository:
git clone https://github.com/skanda0303/QRSUBMISSION.git

cd QRSUBMISSION

Install dependencies:
pip install -r requirements.txt

(Optional) Install YOLOv8 if using advanced detection:
pip install ultralytics

Usage

Place your medicine pack images in the images/ directory.

Run the QR code detection script:
python detect_qr.py --input images/ --output results.json

The output JSON will contain all detected QR codes, their bounding boxes, and values.

Project Structure:
│
├── README.md                # Setup & usage instructions
├── requirements.txt         # Python deps
├── train.py                 #  training script
├── infer.py                 # Must implement inference (input=images → output=JSON)
├── evaluate.py              # (Optional) for self-check with provided GT
│
├── data/                    # (participants don't commit dataset, only placeholder)
│   └── demo_images/         # You’ll provide a small demo set
│
├── outputs/                 
│   ├── submission_detection_1.json   # Required output file (Stage 1)
│   └── submission_decoding_2.json    # Required output file (Stage 2, bonus)
│
└── src/                     # Their actual model code, utils, data loaders, etc.
    ├── models/
    ├── datasets/
    ├── utils/
    └── utils.py
