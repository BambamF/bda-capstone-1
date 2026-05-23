from pathlib import Path
import yt_dlp
import csv
import time
import multiprocessing as mp

Path("videos").mkdir(exist_ok=True)

def download_video(url):
    ydl_options = {
        "outtmpl" : "videos/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])

def read_csv(csv_path, md_path):

    with open(md_path, "w") as mdp:
        with open(csv_path, "r") as csv_pathh:
            reader = csv.DictReader(csv_pathh)
            starter = time.time()
            for row in reader:
                start = time.time()
                download_video(row["url"])
                end = time.time()
                mdp.write("Serial: "+row["title"] + " " + row["url"] + " Download time: " + str(end-start) + " Time Complexity: O(n) " + "Space Complexity: O(n)"+"\n")
            ender = time.time()
            print(f"Serial execution: {ender-starter:.2f}")
            mdp.write(f"Serial download time:  {ender-starter:.2f}, Time Complexity: O(logn), Space Complexity: O(n)"+"\n")
    return ender-starter

def multi_csv(csv_path, md_path):

    with open(md_path, "a") as mdp:
        with open(csv_path, "r") as csv_pathh:
            reader = csv.DictReader(csv_pathh)
            with mp.Pool() as pool:
                start = time.perf_counter()
                columns = [row["url"] for row in reader]
                results = pool.map(download_video, columns)
                end = time.perf_counter()
                parallel_time = round(end-start, 2)
                print(f"Parallel execution: {parallel_time:.2f}")
                mdp.write(f"Parallel download time: {parallel_time:.2f}, Time Complexity: O(logn), Space Complexity: O(n)"+"\n")
    return parallel_time