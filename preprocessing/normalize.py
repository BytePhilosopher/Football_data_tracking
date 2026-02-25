import os
import subprocess
import cv2

# Normalization scales all pixel values into a consistent range 
# so the neural network can learn efficiently and converge faster.
def validate_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        cap.release()
        raise ValueError(f"Cannot open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    cap.release()

    if fps <= 0 or frames <= 0:
        raise ValueError(f"Invalid video metadata: {video_path}")

    return {
        "fps": fps,
        "width": width,
        "height": height,
        "frames": frames,
        "duration": frames / fps
    }


def normalize_video(input_path, output_path,
                    target_fps=25,
                    target_size="1280:720"):

    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-vf", f"scale={target_size}",
        "-r", str(target_fps),
        "-c:v", "libx264",
        "-preset", "veryfast",   # faster
        "-crf", "23",
        "-an",
        output_path
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if result.returncode != 0:
        print(result.stderr.decode())
        raise RuntimeError(f"Normalization failed: {input_path}")

    if not os.path.exists(output_path) or os.path.getsize(output_path) < 10000:
        raise RuntimeError(f"Output invalid: {output_path}")
