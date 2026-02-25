# src/detector.py
from ultralytics import YOLO

class Detector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame)[0]

        boxes = results.boxes.xyxy.cpu().numpy()
        scores = results.boxes.conf.cpu().numpy()
        classes = results.boxes.cls.cpu().numpy()

        detections = []
        for box, score, cls in zip(boxes, scores, classes):
            detections.append({
                "bbox": box,
                "score": float(score),
                "class": int(cls)
            })

        return detections