import os
import json
from ultralytics import YOLO
from glob import glob

# --- Paths ---
MODEL_WEIGHTS =  r"src\models\finalmodelweight.pt"   
TEST_IMAGES_DIR = "QR_DS/test_images"
OUTPUT_JSON = "submission_detection_1.json"

# --- Load model ---
model = YOLO(MODEL_WEIGHTS)

# --- Run inference ---
test_images = glob(os.path.join(TEST_IMAGES_DIR, "*.jpg"))
submission = []

for img_path in test_images:
    results = model.predict(img_path, imgsz=640, conf=0.25, verbose=False)
    qrs = []
    for box in results[0].boxes.xyxy.tolist():  # xyxy format
        x_min, y_min, x_max, y_max = map(float, box)
        qrs.append({"bbox": [x_min, y_min, x_max, y_max]})

    submission.append({
        "image_id": os.path.basename(img_path),
        "qrs": qrs
    })

# --- Save JSON ---
with open(OUTPUT_JSON, "w") as f:
    json.dump(submission, f, indent=2)

print(f"✅ Detection results saved to {OUTPUT_JSON}")
