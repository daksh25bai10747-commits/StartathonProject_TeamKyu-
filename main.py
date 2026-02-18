import cv2
from model import segment_image
from geometry import compute_geometry_score
from utils import compute_material_score

import os
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "data")
BATCH_SIZE = 10

def analysis(img_path):
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError("Image not found. Check path.")

    # 1️ Segmentation
    mask = segment_image(img)

    # 2️ Scoring
    material_score = compute_material_score(mask)
    geometry_score = compute_geometry_score(img)

    total_difficulty = 0.5 * material_score + 0.5 * geometry_score

    bottleneck = "Terrain Geometry" if geometry_score > material_score else "Material Obstacles"

    # 3️ Output
    print("\n===== ENVIRONMENT ANALYSIS =====")
    print(f"Material Score: {material_score:.4f}")
    print(f"Geometry Score: {geometry_score:.4f}")
    print(f"Total Difficulty: {total_difficulty:.4f}")
    print(f"Primary Bottleneck: {bottleneck}")

    

def process_dataset_in_batches():
    images = [f for f in os.listdir(DATASET_DIR)
              if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    total = len(images)
    idx = 0

    while idx < total:
        batch = images[idx: idx + BATCH_SIZE]

        print(f"\n--- Processing images {idx+1} to {min(idx+BATCH_SIZE, total)} of {total} ---")

        for filename in batch:
            img_path = os.path.join(DATASET_DIR, filename)

            img = cv2.imread(img_path)
            if img is None:
                print("Failed to read:", img_path)
                continue

            result = analysis(img_path)  # OR analyze(img)
            print(f"Image: {filename}")
            print("Result:", result)

        idx += BATCH_SIZE

        if idx < total:
            user_input = input("\nProceed further? (y/n): ").strip().lower()
            if user_input != "y":
                print("Stopping further processing.")
                break

    print("\nDone.")

if __name__ == "__main__":
    process_dataset_in_batches()

def save_overlay(img, mask):
    import numpy as np
    heat = cv2.normalize(mask.astype("float"), None, 0, 255, cv2.NORM_MINMAX)
    heat = cv2.applyColorMap(heat.astype("uint8"), cv2.COLORMAP_JET)
    overlay = cv2.addWeighted(img, 0.7, heat, 0.3, 0)
    cv2.imwrite("overlay.jpg", overlay)
    print("Saved overlay.jpg")

