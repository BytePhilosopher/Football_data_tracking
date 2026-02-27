import os
import csv
import numpy as np # Added for potential numpy operations if needed
from supervision.detection.core import Detections # To type hint

class MetadataLogger:
    def __init__(self, output_dir="data/annotations"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.output_file = os.path.join(output_dir, "metadata.csv") # Correctly defines the output file path
        self.metadata_rows = []
        # Define CSV header including object_id for tracking
        self.header = ["frame_id", "object_id", "class_id", "confidence", "bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2"]

    def log(self, frame_id: int, detections: Detections):
        # Iterate through each detected object's properties
        # Ensure detections has track_id for tracking data
        if detections.tracker_id is not None:
            for i in range(len(detections.xyxy)):
                object_id = detections.tracker_id[i]
                class_id = detections.class_id[i]
                confidence = detections.confidence[i]
                x1, y1, x2, y2 = detections.xyxy[i]

                row = [
                    frame_id,
                    int(object_id),
                    int(class_id),
                    float(confidence),
                    float(x1), float(y1), float(x2), float(y2)
                ]
                self.metadata_rows.append(row)
        else:
            # Handle cases where there's detection but no tracking ID yet (e.g., first frame or no tracker)
            for i in range(len(detections.xyxy)):
                class_id = detections.class_id[i]
                confidence = detections.confidence[i]
                x1, y1, x2, y2 = detections.xyxy[i]
                row = [
                    frame_id,
                    -1, # Indicate no object_id yet if tracker_id is None
                    int(class_id),
                    float(confidence),
                    float(x1), float(y1), float(x2), float(y2)
                ]
                self.metadata_rows.append(row)

    def save(self):
        with open(self.output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)
            writer.writerows(self.metadata_rows)
        print(f"Metadata saved to: {self.output_file}")

    def close(self):
        self.save()