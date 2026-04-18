from moviepy.editor import VideoFileClip
import os

def create_clips(video_path, highlights):
    video = VideoFileClip(video_path)
    clips = []

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, "outputs")

    for i, (start, end) in enumerate(highlights):
        clip = video.subclip(start, end)
        clip = clip.set_fps(15)

        output_path = os.path.join(output_dir, f"clip_{i}.mp4")

        clip.write_videofile(
            output_path,
            codec="libx264",
            preset="ultrafast",
            audio=False
        )

        clips.append(output_path)

    return clips