def detect_highlights(segments):
    highlights = []

    for seg in segments:
        text = seg["text"].lower()
        score = 0

        keywords = ["important", "secret", "mistake", "learn"]

        if any(word in text for word in keywords):
            score += 1

        if len(text.split()) > 8:
            score += 1

        if score >= 1:
            highlights.append((seg["start"], seg["end"]))

    return highlights[:2]