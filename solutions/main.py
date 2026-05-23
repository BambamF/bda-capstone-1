from library import download_video, read_csv, multi_csv
import time
import os

url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
csv_path = "data/video_urls.csv"

relative_path = os.getcwd()

reports_path = os.path.join(relative_path, "reports/reports.md")


if __name__ == "__main__":
    read_run = read_csv(csv_path, reports_path)
    multi_run = multi_csv(csv_path, reports_path)
    with open(reports_path, "a") as rp:
        rp.write(f"Improvement from multiprocessing: {read_run - multi_run:.2f}")