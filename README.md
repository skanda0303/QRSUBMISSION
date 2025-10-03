Multi-QR Code Recognition for Medicine Packs

Project Overview:
Multi-QR Code Recognition System to detect and decode multiple QR codes from images of medicine packs.

Key Features:
- Detect multiple QR codes in a single image
- Extract QR code values and types
- Provide bounding box coordinates
- Export results in JSON format
- Batch processing supported

Technology Stack:
- Python 3.10+
- OpenCV
- PyTorch / YOLOv8 (optional)
- JSON output

Project Structure:
README.md
requirements.txt
train.py
infer.py
evaluate.py
data/
demo_images/
outputs/
submission_detection_1.json
submission_decoding_2.json
src/
models/
datasets/
utils.py

Installation:
1. Clone the repository:
git clone https://github.com/skanda0303/QRSUBMISSION.git
cd QRSUBMISSION

2. Install dependencies:
pip install -r requirements.txt

3. Install YOLOv8 (optional):
pip install ultralytics

Usage:
1. Prepare images:
Place your medicine pack images into the images/ directory.

2. Run detection and decoding:
python infer.py --input images/ --output results.json

Example Output:
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
