# src/tracker.py
import supervision as sv
import numpy as np

class Tracker:
    def __init__(self):
        self.tracker = sv.ByteTrack()

    def update(self, detections):
        if len(detections) == 0:
            return []

        boxes = np.array([d["bbox"] for d in detections])
        scores = np.array([d["score"] for d in detections])
        classes = np.array([d["class"] for d in detections])

        sv_detections = sv.Detections(
            xyxy=boxes,
            confidence=scores,
            class_id=classes
        )

        tracked = self.tracker.update_with_detections(sv_detections)

        output = []
        for box, track_id, cls in zip(
            tracked.xyxy,
            tracked.tracker_id,
            tracked.class_id
        ):
            output.append({
                "bbox": box,
                "track_id": int(track_id),
                "class": int(cls)
            })

        return output