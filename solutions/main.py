from library import download_video, read_csv, multi_csv, extract_video_metadata
import time
import os
import csv

csv_path = "data/video_urls.csv"

relative_path = os.getcwd()

reports_path = os.path.join(relative_path, "reports/reports.md")


if __name__ == "__main__":
    with open(csv_path, "r") as csv_p:
        reader = csv.DictReader(csv_p)
        urls = [row["url"] for row in reader]
    metadata_rows, status = extract_video_metadata(urls)
    if status["status"].lower() == "success":
        with open("data/video_metadata.csv", "w", newline="") as file:
            fieldnames = ["title", "duration", "uploader", "view_count", "ext", "url", 'filesize', 'uploader_url', 'extractor_key', '_format_sort_fields', 'playable_in_embed', 'quality', 'tbr', 'asr', 'thumbnail', 'downloader_options', 'vbr', 'available_at', 'tags', 'channel_id', 'heatmap', 'availability', 'vcodec', 'acodec', 'channel_url', 'average_rating', 'was_live', 'protocol', 'aspect_ratio', 'has_drm', 'format', 'release_year', 'display_id', 'live_status', 'location', 'uploader_id', 'format_note', 'format_id', 'original_url', 'formats', 'comment_count', 'fps', 'playlist', 'width', 'categories', 'is_live', 'resolution', 'age_limit', 'upload_date', 'extractor', 'duration_string', 'channel', 'abr', 'creators', 'source_preference', 'dynamic_range', 'video_ext', 'epoch', 'audio_ext', 'requested_subtitles', '_has_drm', 'language', 'chapters', 'webpage_url', 'audio_channels', 'release_timestamp', 'like_count', 'channel_follower_count', 'playlist_index', 'preference', 'webpage_url_basename', 'timestamp', 'subtitles', 'channel_is_verified', 'filesize_approx', 'description', 'language_preference', 'fulltitle', 'automatic_captions', 'height', 'id', 'http_headers', 'media_type', 'webpage_url_domain', 'thumbnails' ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(metadata_rows)
        read = read_csv(csv_path, reports_path)
        multi = multi_csv(csv_path, reports_path)
        with open(reports_path, "a") as r_p2:
            r_p2.write(f"Improvement from multiprocessing: {read - multi:.2f}")
    else:
        print(f"Error Status: {status["error"]}")