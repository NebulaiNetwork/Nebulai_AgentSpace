"""
EmotionAgent
------------
Detects and interprets emotional tone and sentiment in text for empathetic responses.
"""
&nbsp;
&nbsp;

from textblob import TextBlob
&nbsp;
&nbsp;

class EmotionAgent:
    def __init__(self):
        pass
&nbsp;
&nbsp;

    def detect_emotion(self, text: str) -> str:
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0.5:
            emotion = "Positive (e.g. happiness, excitement)"
        elif polarity < -0.5:
            emotion = "Negative (e.g. sadness, anger)"
        else:
            emotion = "Neutral or mixed"
        return f"Detected emotion: {emotion}"
