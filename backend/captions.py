def generate_captions(segments):
    captions = []
    for seg in segments:
        captions.append({
            "start": seg["start"],
            "text": seg["text"]
        })
    return captions