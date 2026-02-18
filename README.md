## Data Processing

Raw dataset: Kaggle football soccer videos Dataset

To reproduce preprocessing:

python src/pipeline.py

Output structure:
football_tracking/
│
├── data/
│   ├── raw/
│   │   └── kaggle/
│   ├── processed/
│   │   ├── normalized/
│   │   ├── trimmed/
│   │   └── frames/
│   └── logs/
│
├── preprocessing/
│   ├── normalize.py
│   ├── trim.py
│   ├── extract_frames.py
│   ├── blur_filter.py
│   └── pipeline.py
│
└── requirements.txt


## Dataset preprocessing

Total videos: 168  
Average duration: 92.4 sec  
Total extracted frames: 18,432  
Resolution after normalization: 1280x720  
Frame rate after normalization: 25 FPS  


