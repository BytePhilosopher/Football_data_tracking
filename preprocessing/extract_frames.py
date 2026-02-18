import cv2
import os
from tqdm import tqdm

def extract_frames(video_path, output_dir, frame_rate=2):

    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Cannot open: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        raise ValueError("Invalid FPS")

    interval = max(int(fps / frame_rate), 1)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_count = 0
    saved_count = 0

    with tqdm(total=total_frames, desc="Extracting") as pbar:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % interval == 0:
                out_path = os.path.join(
                    output_dir,
                    f"frame_{saved_count:05d}.jpg"
                )
                cv2.imwrite(out_path, frame)
                saved_count += 1

            frame_count += 1
            pbar.update(1)

    cap.release()
