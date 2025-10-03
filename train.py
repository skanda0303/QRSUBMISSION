# train.py

import os
import zipfile
import argparse
import shutil
from ultralytics import YOLO

# --- Configuration ---
ZIP_FILE_NAME = 'src/datasets/QR_DS-20251002T130757Z-1-001.zip'
EXTRACTION_DIR_ROOT = 'data'
EXTRACTED_DATA_DIR = os.path.join(EXTRACTION_DIR_ROOT, 'QR_DS')
DATA_YAML_PATH = os.path.join(EXTRACTED_DATA_DIR, 'data.yaml')
FINAL_MODEL_PATH = "src/models/finalmodelweight.pt"  # <- your desired final location


def setup_data():
    """Handles ZIP extraction and creates the data.yaml file."""
    if not os.path.exists(EXTRACTED_DATA_DIR):
        print(f"Creating data directory: {EXTRACTION_DIR_ROOT}")
        os.makedirs(EXTRACTION_DIR_ROOT, exist_ok=True)

    zip_path = ZIP_FILE_NAME
    if os.path.exists(zip_path):
        print(f"Extracting {ZIP_FILE_NAME} to {EXTRACTION_DIR_ROOT}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(EXTRACTION_DIR_ROOT)
        print("Extraction complete.")
    else:
        print(f"FATAL ERROR: ZIP file '{ZIP_FILE_NAME}' not found. Cannot set up data.")
        return

    # Create the data.yaml file
    yaml_content = f"""
path: {EXTRACTED_DATA_DIR}
train: train_images/images
val: {EXTRACTED_DATA_DIR}/valid_images/images
test: {EXTRACTED_DATA_DIR}/test_images

nc: 1
names: ['qr_codes']
"""
    with open(DATA_YAML_PATH, "w") as f:
        f.write(yaml_content)

    print(f"✅ data.yaml created successfully at: {DATA_YAML_PATH}")


def train_model():
    """Loads and trains the YOLOv8 model."""
    if not os.path.exists(DATA_YAML_PATH):
        print("ERROR: data.yaml not found. Please run 'python train.py --setup_data' first.")
        return

    # Load YOLOv8 nano model. It will auto-download weights if needed.
    model = YOLO("yolov8n.pt")

    print("## Starting YOLOv8 Training... Please Wait.")
    results = model.train(
        data=DATA_YAML_PATH,
        epochs=50,
        imgsz=640,
        batch=32,
        patience=20,
        name="qr_yolo_model",
        device=0  # Use GPU
    )

    # YOLO saves to runs/detect/qr_yolo_model/weights/best.pt
    best_weights_path = os.path.join(results.save_dir, "weights", "best.pt")

    # Copy weights to your desired location
    os.makedirs(os.path.dirname(FINAL_MODEL_PATH), exist_ok=True)
    shutil.copy(best_weights_path, FINAL_MODEL_PATH)

    print(f"### Training Finished! 🎉 Best weights copied to: {FINAL_MODEL_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 QR Code Training Script")
    parser.add_argument("--setup_data", action="store_true", help="Extracts data and creates data.yaml")

    args = parser.parse_args()

    if args.setup_data:
        setup_data()
    else:
        train_model()
