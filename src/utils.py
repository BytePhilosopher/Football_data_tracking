import cv2
import supervision as sv

CLASS_COLORS = {
    0: (255, 0, 0),    # team_1 → Blue
    1: (0, 0, 255),    # team_2 → Red
    2: (0, 255, 255),  # goalkeeper → Yellow
    3: (0, 255, 0),    # referee → Green
    4: (255, 255, 255) # ball → White
}

CLASS_NAMES = {
    0: "Team 1",
    1: "Team 2",
    2: "Goalkeeper",
    3: "Referee",
    4: "Ball"
}

def draw_boxes(frame, detections: sv.Detections):

    # Ensure there are detections to draw
    if detections is None or len(detections.xyxy) == 0:
        return frame

    # Iterate through the detections object attributes
    for i in range(len(detections.xyxy)):
        x1, y1, x2, y2 = map(int, detections.xyxy[i])
        # Handle cases where tracker_id might not be available yet
        track_id = detections.tracker_id[i] if detections.tracker_id is not None and len(detections.tracker_id) > i else -1
        class_id = detections.class_id[i]

        color = CLASS_COLORS.get(class_id, (200, 200, 200))
        label = CLASS_NAMES.get(class_id, "Unknown")

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        cv2.putText(
            frame,
            f"{label} | ID {track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            2
        )

    return frame