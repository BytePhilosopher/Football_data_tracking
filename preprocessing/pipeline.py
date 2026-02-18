import os
from normalize import normalize_video
from Trim import trim_video
from extract_frames import extract_frames
from blur_filter import remove_blurry_frames

RAW_DIR = "data/raw/kaggle"
NORMALIZED_DIR = "data/processed/normalized"
TRIMMED_DIR = "data/processed/trimmed"
FRAMES_DIR = "data/processed/frames"

os.makedirs(NORMALIZED_DIR, exist_ok=True)
os.makedirs(TRIMMED_DIR, exist_ok=True)
os.makedirs(FRAMES_DIR, exist_ok=True)


def run_pipeline():

    video_files = [
        f for f in os.listdir(RAW_DIR)
        if f.endswith(".mp4")
    ]

    for video_file in video_files:

        print(f"\nProcessing: {video_file}")

        raw_path = os.path.join(RAW_DIR, video_file)
        name = os.path.splitext(video_file)[0]

        normalized_path = os.path.join(NORMALIZED_DIR, f"{name}_norm.mp4")
        trimmed_path = os.path.join(TRIMMED_DIR, f"{name}_trim.mp4")
        frames_output = os.path.join(FRAMES_DIR, name)

        if os.path.exists(trimmed_path):
            print("Already processed. Skipping.")
            continue

        try:
            normalize_video(raw_path, normalized_path)
            trim_video(normalized_path, trimmed_path, 10, 120)
            extract_frames(trimmed_path, frames_output, frame_rate=2)
            remove_blurry_frames(frames_output)

            print("Success.")

        except Exception as e:
            print(f"Failed on {video_file}: {e}")


if __name__ == "__main__":
    run_pipeline()
