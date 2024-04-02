from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from datetime import datetime

def convert_time_to_seconds(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
    return seconds

def trim_video(input_file, output_file, start_time, end_time):
    try:
        start_seconds = convert_time_to_seconds(start_time)
        end_seconds = convert_time_to_seconds(end_time)
        ffmpeg_extract_subclip(input_file, start_seconds, end_seconds, targetname=output_file)
        print("Video trimmed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "2024-04-02 12-32-32.mkv"  # Input video file (MKV)
    output_file = "output_video.mkv"  # Output video file (MKV)
    start_time = "00:00:00"  # Start time in HH:MM:SS format
    end_time = "00:00:52"  # End time in HH:MM:SS format
    
    trim_video(input_file, output_file, start_time, end_time)

