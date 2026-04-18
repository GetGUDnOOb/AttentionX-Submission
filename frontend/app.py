import streamlit as st
import requests

st.title("🎬 AttentionX")

video = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"])

if video:
    st.info("Processing...")

    files = {"file": video}

    try:
        res = requests.post("http://127.0.0.1:8000/process/", files=files)
        data = res.json()

        if data.get("status") == "success":
            st.success("✅ Clips Generated!")

            for clip_url in data["clips"]:
                st.video(clip_url)

        else:
            st.error("❌ Backend Error")
            st.write(data.get("message", "Unknown error"))

    except Exception as e:
        st.error("❌ Failed to connect to backend")
        st.write(str(e))