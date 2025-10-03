import os
import json
import cv2
import numpy as np
from pathlib import Path
from ultralytics import YOLO

# --- Paths ---
MODEL_WEIGHTS =  r"src\models\finalmodelweight.pt"    # replace with your trained weights
TEST_IMAGES_DIR = "data/demo_images"
OUTPUT_JSON = "submission_decoding_2.json"

# --- Classification Logic ---
def classify_qr_content(value: str) -> str:
    value = str(value).strip().upper()
    if value.startswith('(01)') or value.startswith('(10)'):
        return "GS1/Batch Code"
    if len(value) == 8 and all(c.isalnum() for c in value):
        return "Product/Serial ID"
    if value.startswith("B"):
        return "Batch"
    if value.startswith("MFR"):
        return "Manufacturer"
    return "Unclassified/Other"

# --- Decode QR from bounding box ---
def decode_qr_from_bbox(img: np.ndarray, bbox: list) -> tuple[str, str]:
    x_min, y_min, x_max, y_max = [int(round(c)) for c in bbox]
    margin = 5
    crop = img[
        max(0, y_min - margin) : min(img.shape[0], y_max + margin),
        max(0, x_min - margin) : min(img.shape[1], x_max + margin)
    ]

    detector = cv2.QRCodeDetector()
    value, _, _ = detector.detectAndDecode(crop)

    if value:
        return value, classify_qr_content(value)
    return "", "Other"

# --- Load YOLO model ---
model = YOLO(MODEL_WEIGHTS)

# --- Inference + Classification ---
submission = []
for img_path in Path(TEST_IMAGES_DIR).glob("*.jpg"):
    img = cv2.imread(str(img_path))
    result = model.predict(img, imgsz=640, conf=0.25, verbose=False)[0]

    qrs_list = []
    for box in result.boxes.xyxy.cpu().numpy():
        x_min, y_min, x_max, y_max = box.tolist()
        decoded_value, qr_type = decode_qr_from_bbox(img, box.tolist())
        qrs_list.append({
            "bbox": [x_min, y_min, x_max, y_max],
            "value": decoded_value,
            "type": qr_type
        })

    submission.append({
        "image_id": img_path.name,
        "qrs": qrs_list
    })

# --- Save JSON ---
with open(OUTPUT_JSON, "w") as f:
    json.dump(submission, f, indent=4)

print(f"✅ Detection + Classification results saved to {OUTPUT_JSON}")

