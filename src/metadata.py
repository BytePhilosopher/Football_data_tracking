# src/metadata.py
import csv
import os

class MetadataLogger:
    def __init__(self, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.file = open(output_path, mode='w', newline='')
        self.writer = csv.writer(self.file)

        self.writer.writerow([
            "frame_id",
            "track_id",
            "class",
            "x1", "y1", "x2", "y2"
        ])

    def log(self, frame_id, tracked_objects):
        for obj in tracked_objects:
            x1, y1, x2, y2 = obj["bbox"]
            self.writer.writerow([
                frame_id,
                obj["track_id"],
                obj["class"],
                x1, y1, x2, y2
            ])

    def close(self):
        self.file.close()