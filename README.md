# 🎬 AttentionX – AI Content Repurposing Engine

Turn long-form videos into short, viral-ready clips automatically using AI.

---

## 🚀 Features

* 🎤 Speech-to-text using Whisper
* ✂️ Automatic highlight detection
* 🎬 Clip generation (short-form videos)
* ⚡ Fast processing (optimized for demo)
* 🌐 Web interface using Streamlit
* 📡 Backend API using FastAPI

---

## 🎥 Demo Video

Watch how AttentionX converts long videos into short clips 👇

👉 **[▶️ Watch Demo Video](https://drive.google.com/file/d/13h1PZ3eVrG-4yqqYDZbcitJeSTYicbcu/view?usp=drive_link)**

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **AI Model:** OpenAI Whisper
* **Video Processing:** MoviePy
* **Language:** Python

---

## 📁 Project Structure

```
attentionx/
│
├── backend/
│   ├── main.py
│   ├── transcription.py
│   ├── highlight.py
│   ├── video_edit.py
│   └── __init__.py
│
├── frontend/
│   └── app.py
│
├── uploads/
├── outputs/
├── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone <your-repo-link>
cd attentionx
```

---

### 2. Install dependencies

```
pip install fastapi uvicorn streamlit moviepy opencv-python mediapipe openai-whisper requests python-multipart
```

---

### 3. Install FFmpeg (IMPORTANT)

Download from: https://ffmpeg.org/download.html

Add to system PATH:

```
C:\ffmpeg\bin
```

Verify installation:

```
ffmpeg -version
```

---

## ▶️ How to Run

### Step 1: Start Backend

```
python backend/main.py
```

Server runs at:

```
http://127.0.0.1:8000
```

---

### Step 2: Start Frontend

```
streamlit run frontend/app.py
```

---

## 🎬 How It Works

1. Upload a video
2. Backend processes it
3. AI extracts highlights
4. Short clips are generated
5. Clips are displayed in UI

---

## ⚡ Fast Mode (Demo Optimized)

* Limits video to 30 seconds
* Uses predefined highlights
* Faster processing for demos

---

## 📦 Output

Generated clips are saved in:

```
outputs/
```

---

## 🧪 Example Output

* clip_0.mp4
* clip_1.mp4

---



---

## 🔥 Future Improvements

* 🎬 Auto subtitles
* 🔥 Viral hook generation
* 📱 Vertical video formatting
* 🧠 Advanced AI highlight detection

---

## 📜 License

This project is for educational and hackathon use.

---

## 👨‍💻 Author

Built for AI Hackathon 🚀
