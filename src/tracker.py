# src/tracker.py
import supervision as sv
import numpy as np

import supervision as sv
import numpy as np

class Tracker:
    def __init__(self):
        self.tracker = sv.ByteTrack()

    def update(self, detections):
        # 'detections' here is expected to be ultralytics.engine.results.Boxes
        # Check if there are any detections before trying to extract data
        if detections is not None and len(detections) > 0:
            # Extract bounding boxes, confidence scores, and class IDs
            # Convert tensors to numpy arrays on CPU
            xyxy = detections.xyxy.cpu().numpy()
            confidence = detections.conf.cpu().numpy()
            class_id = detections.cls.cpu().numpy().astype(int)

            # Create Supervision Detections object
            sv_detections = sv.Detections(
                xyxy=xyxy,
                confidence=confidence,
                class_id=class_id
            )
        else:
            # If no detections, return an empty sv.Detections object
            sv_detections = sv.Detections(
                xyxy=np.empty((0, 4)),
                confidence=np.array([]),
                class_id=np.array([])
            )

        # Apply ByteTrack for object tracking
        tracked_detections = self.tracker.update_with_detections(sv_detections)
        return tracked_detections