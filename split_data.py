import os
import shutil
from glob import glob

SOURCE_FOLDER = "raw"
TARGET_FOLDER = "data"

# Create target directories
for split in ["train", "test"]:
    for class_id in range(14):
        os.makedirs(f"{TARGET_FOLDER}/{split}/{class_id}", exist_ok=True)

for class_id in range(14):
    folder = f"{SOURCE_FOLDER}/Gesture_{class_id}"
    images = glob(f"{folder}/*.*")

    # sort filenames numerically
    images = sorted(images, key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))

    # split
    train_imgs = images[:800]
    test_imgs = images[800:]

    # copy
    for img in train_imgs:
        shutil.copy(img, f"{TARGET_FOLDER}/train/{class_id}/")

    for img in test_imgs:
        shutil.copy(img, f"{TARGET_FOLDER}/test/{class_id}/")

print("Dataset prepared successfully!")
