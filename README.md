# Multi-QR Code Recognition for Medicine Packs 💊

# This project works only with python 3.10

## 📄 Project Overview
This project is a **Multi-QR Code Recognition System** designed to accurately detect and decode multiple QR codes from images of medicine packs. Given that many medicine packages contain multiple codes (for manufacturers, batch numbers, distributors, and regulators), this system aims to detect all QR codes in a single image, extracting their values and precise positions.

---

## ✨ Key Features
* Detect multiple QR codes in a single image.
* Extract QR code values and classify their type.
* Provide **bounding box coordinates** for each QR code.
* Export results in structured **JSON** format.
* Supports batch processing of multiple images.

---

## ⚙️ Technology Stack
| Component | Details |
| :--- | :--- |
| **Language** | Python 3.10 only |
| **Core Libraries** | OpenCV (for image processing and decoding) |
| **Advanced Detection** | PyTorch / YOLOv8  |
| **Output Format** | JSON (for structured results) |

---

## 📂 Project Structure
```text
QRSUBMISSION/
│
├── README.md                 # Setup & usage instructions (This file)
├── requirements.txt          # Python dependencies
├── train.py                  # Training script
├── infer.py                  # Core inference script (Input: images → Output: JSON)
├── evaluate.py               # (Optional) for self-check with provided GT
│
├── data/                     # Placeholder for the dataset
│   └── demo_images/         # Small demo set
│
├── outputs/                  # Location for generated results and submission files
│   ├── submission_detection_1.json    # Required output file (Stage 1)
│   └── submission_decoding_2.json     # Required output file (Stage 2, bonus)
│
└── src/                      # Actual model code, utilities, etc.
    ├── models/
    ├── datasets/
    └── utils.py


## 🚀 Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/skanda0303/QRSUBMISSION.git
cd QRSUBMISSION ```

2. Install dependencies
```bash
pip install -r requirements.txt```












- **Stage 1:** `outputs/submission_detection_1.json` - QR code bounding box predictions
- **Stage 2:** `outputs/submission_decoding_2.json` - Decoded QR codes with type classification



