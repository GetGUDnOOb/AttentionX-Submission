from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
import shutil
import os

from backend.transcription import transcribe
from backend.highlight import detect_highlights
from backend.video_edit import create_clips
from moviepy.editor import VideoFileClip

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Serve videos
app.mount("/videos", StaticFiles(directory=OUTPUT_DIR), name="videos")


@app.get("/")
def home():
    return {"message": "AttentionX API is running"}


@app.post("/process/")
async def process_video(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Limit to 30 seconds
        video = VideoFileClip(file_path)
        if video.duration > 30:
            short_path = file_path.replace(".mp4", "_short.mp4")
            video.subclip(0, 30).write_videofile(short_path, codec="libx264", preset="ultrafast")
            file_path = short_path

        # FAST demo mode (no whisper delay)
        highlights = [(0, 10), (10, 20)]

        clips = create_clips(file_path, highlights)

        # Convert to URLs
        clip_urls = []
        for clip in clips:
            filename = os.path.basename(clip)
            clip_urls.append(f"http://127.0.0.1:8000/videos/{filename}")

        return {"status": "success", "clips": clip_urls}

    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)