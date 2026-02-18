from SoccerNet.Downloader import SoccerNetDownloader

# Change this path to where you want to store SoccerNet data
LOCAL_DIR = "SoccerNetData"

downloader = SoccerNetDownloader(LocalDirectory=LOCAL_DIR)

# This downloads the SoccerNet tracking task dataset
downloader.downloadDataTask(
    task="tracking",
    split=["train", "test", "challenge"]
)

# Optionally download the tracking data for a specific challenge release if available
downloader.downloadDataTask(
    task="tracking-2023",
    split=["train", "test", "challenge"]
)

print("Download attempted — check logs for status")
