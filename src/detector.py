# src/detector.py
from ultralytics import YOLO
import numpy as np

from ultralytics import YOLO
import numpy as np

class Detector:
    def __init__(self, model_path, conf=0.4):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame):
        results = self.model(frame, conf=self.conf)[0] # results is an ultralytics.engine.results.Results object
        return results.boxes # This is an ultralytics.engine.results.Boxes object