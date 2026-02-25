import cv2
import os

from src.preprocess import preprocess_video
from src.detector import Detector
from src.tracker import Tracker
from src.metadata import MetadataLogger
from src.utils import draw_boxes

RAW_VIDEO = "data/raw/kaggle/168.mp4"
PROCESSED_VIDEO = "data/processed/168_processeded.mp4"
MODEL_PATH = "yolov8m.pt"

# Step 1: Preprocess
preprocess_video(RAW_VIDEO, PROCESSED_VIDEO)

# Step 2: Load modules
detector = Detector(MODEL_PATH)
tracker = Tracker()
logger = MetadataLogger("data/annotations/tracking.csv")

cap = cv2.VideoCapture(PROCESSED_VIDEO)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    "data/processed/output.mp4",
    fourcc,
    15,
    (1280, int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
)

frame_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detector.detect(frame)
    tracked = tracker.update(detections)

    logger.log(frame_id, tracked)

    annotated = draw_boxes(frame, tracked)
    out.write(annotated)

    frame_id += 1

cap.release()
out.release()
logger.close()