import cv2
import os

def preprocess_video(input_path, output_path, target_fps=15, resize_width=1280):
    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Cannot open video file: {input_path}")

    original_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = max(1, int(original_fps / target_fps))

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if width == 0 or height == 0:
        raise ValueError("Failed to read frame dimensions. Check input video.")

    scale = resize_width / width
    new_height = int(height * scale)

    # macOS-friendly codec
    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H.264
    out = cv2.VideoWriter(output_path, fourcc, target_fps, (resize_width, new_height))

    if not out.isOpened():
        raise IOError(f"Cannot write to output video: {output_path}")

    print(f"Processing video: {input_path} -> {output_path}")
    print(f"Original FPS: {original_fps}, Target FPS: {target_fps}, Frame interval: {frame_interval}")
    print(f"Resolution: {resize_width}x{new_height}")

    frame_id = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_id % frame_interval == 0:
            frame = cv2.resize(frame, (resize_width, new_height))
            out.write(frame)

        frame_id += 1

    cap.release()
    out.release()
    print(f"Video saved successfully: {output_path}")


if __name__ == "__main__":
    preprocess_video(
        "data/raw/kaggle/168.mp4",
        "data/processed/168_processeded.mp4"
    )