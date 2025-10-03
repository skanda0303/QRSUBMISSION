# Multi-QR Code Recognition for Medicine Packs 💊

> **Note:** This project works only with Python 3.10

---

## 📄 Project Overview
This project is a **Multi-QR Code Recognition System** designed to accurately detect and decode multiple QR codes from images of medicine packs.  
Many medicine packages contain multiple codes (for manufacturers, batch numbers, distributors, and regulators). This system detects all QR codes in a single image and extracts their values and precise positions.

---

## ✨ Key Features
- Detect multiple QR codes in a single image
- Extract QR code values and classify their type
- Provide **bounding box coordinates** for each QR code
- Export results in structured **JSON** format
- Supports batch processing of multiple images

---

## ⚙️ Technology Stack

| Component           | Details                                |
|--------------------|----------------------------------------|
| **Language**        | Python 3.10 only                       |
| **Core Libraries**  | OpenCV (for image processing & decoding) |
| **Advanced Detection** | PyTorch / YOLOv8                       |
| **Output Format**   | JSON (structured results)              |

---

## 📂 Project Structure
```text
QRSUBMISSION/
│
├── README.md                    # Setup & usage instructions (this file)
├── requirements.txt             # Python dependencies
├── train.py                     # Training script
├── infer.py                      # Core inference script (Input: images → Output: JSON)
├── evaluate.py                  # Optional: Self-check with provided ground truth
│
├── data/                        # Placeholder for the dataset
│   └── demo_images/             # Small demo set
│
├── outputs/                     # Generated results and submission files
│   ├── submission_detection_1.json    # Stage 1: QR code bounding box predictions
│   └── submission_decoding_2.json     # Stage 2: Decoded QR codes with type classification
│
└── src/                         # Actual model code and utilities
    ├── models/
    ├── datasets/
    └── utils.py
```


## 🚀 Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/skanda0303/QRSUBMISSION.git
cd QRSUBMISSION
```

2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Install YOLOv8 (optional)
```bash
pip install ultralytics
```
Usage

1. Prepare images
Place the test images in data folder and change the directory in infer.py and infer1.py respectively 

2. Run detection and decoding
```bash
python infer.py --input images/ --output results.json
```
3. Run the infer.py
```bash
python infer1.py --input data/ --output outputs/submission_detection.json
```
4. Run the infer1.py
```bash
python infer1.py --input data/ --output outputs/submission_decoding2.json
```
















