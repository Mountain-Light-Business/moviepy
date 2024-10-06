import os
from moviepy.editor import VideoFileClip, AudioFileClip

def mp4_to_mp3(mp4_files):
    for mp4_file in mp4_files:
        try:
            # Extracting the file name without the extension
            file_name = os.path.splitext(os.path.basename(mp4_file))[0]
            mp3_output = f"{file_name}.mp3"

            # Converting video to audio
            video_clip = VideoFileClip(mp4_file)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile("output/" + mp3_output)

            # Closing audio and video clip instances
            audio_clip.close()
            video_clip.close()

            # Output info
            print(f"{mp4_file} has been successfully converted to {mp3_output}")
        except Exception as e:
            print(f"Error converting {mp4_file} to MP3: {str(e)}")

# Example usage for multiple files:
mp4_files = [
    "videos/OP_MG_LESS34.mp4",
    "videos/OP_MG_LESS23.mp4",
    "videos/OP_MG_LESS29.mp4",
    "videos/OP_MG_LESS35.mp4",
    "videos/OP_MG_LESS30.mp4"
]

# Convert the MP4 files to MP3 using the same names
mp4_to_mp3(mp4_files)
