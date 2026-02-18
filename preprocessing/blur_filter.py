import cv2
import os

def is_blurry(image_path, threshold=100):

    img = cv2.imread(image_path)

    if img is None:
        return True

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()

    return variance < threshold


def remove_blurry_frames(frames_dir, threshold=100):

    for file in os.listdir(frames_dir):

        path = os.path.join(frames_dir, file)

        if not file.lower().endswith(".jpg"):
            continue

        if is_blurry(path, threshold):
            os.remove(path)
