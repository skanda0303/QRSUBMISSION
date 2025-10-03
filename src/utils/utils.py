# src/utils.py

import cv2
import numpy as np

def classify_qr_content(value: str) -> str:
    """
    Custom logic to classify the QR code based on content patterns.
    **Refine these rules based on your data analysis for a better bonus score!**
    """
    value = str(value).strip().upper()
    if value.startswith('MFR') or 'MANUFACTURER' in value:
        return "Manufacturer Code"
    elif value.startswith('LOT') or 'BATCH' in value:
        return "Batch/Lot Number"
    elif value.startswith(('REG', 'ID')) or len(value) > 10:
        return "Regulatory/Serial ID"
    else:
        return "Other"

def decode_qr_from_bbox(img: np.ndarray, bbox: list) -> tuple[str, str]:
    """
    Crops the image based on the detected bounding box and attempts to decode 
    the QR code using the OpenCV decoder.
    """
    if img is None: 
        return "Failed to decode", "Failed"
    
    # Bbox: [x_min, y_min, x_max, y_max]
    x_min, y_min, x_max, y_max = [int(round(c)) for c in bbox]
    
    # Add a small margin for robust decoding
    margin = 5
    crop = img[
        max(0, y_min - margin) : min(img.shape[0], y_max + margin),
        max(0, x_min - margin) : min(img.shape[1], x_max + margin)
    ]
    
    # Initialize and use the OpenCV decoder
    detector = cv2.QRCodeDetector()
    value, points, _ = detector.detectAndDecode(crop)
    
    if value:
        classification_type = classify_qr_content(value)
        return value, classification_type
    else:
        return "Failed to decode", "Failed"