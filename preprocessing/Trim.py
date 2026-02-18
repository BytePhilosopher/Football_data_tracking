import os
import subprocess
from normalize import validate_video

def trim_video(input_path, output_path, start_sec, end_sec):

    info = validate_video(input_path)

    if start_sec >= info["duration"]:
        raise ValueError("Start time exceeds duration")

    end_sec = min(end_sec, info["duration"])
    clip_duration = end_sec - start_sec

    command = [
        "ffmpeg",
        "-y",
        "-ss", str(start_sec),
        "-i", input_path,
        "-t", str(clip_duration),
        "-c:v", "libx264",
        "-preset", "veryfast",
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
        raise RuntimeError(f"Trimming failed: {input_path}")
