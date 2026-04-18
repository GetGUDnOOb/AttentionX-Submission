import whisper

model = whisper.load_model("tiny")

def transcribe(video_path):
    result = model.transcribe(video_path)
    return result["segments"]