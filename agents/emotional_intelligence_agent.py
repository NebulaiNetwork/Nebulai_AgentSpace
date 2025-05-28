"""
EmotionalIntelligenceAgent
--------------------------
Recognizes, interprets, and appropriately responds to human emotional states.
"""
&nbsp;
&nbsp;

from textblob import TextBlob
&nbsp;
&nbsp;

class EmotionalIntelligenceAgent:
    def __init__(self):
        pass
&nbsp;
&nbsp;

    def analyze_emotion(self, text: str) -> str:
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.4:
            return "Emotion detected: Happy/Positive"
        elif polarity  -0.4:
            return "Emotion detected: Sad/Negative"
        else:
            return "Emotion detected: Neutral/Mixed"
&nbsp;
&nbsp;

    def respond_with_empathy(self, emotion: str) -> str:
        responses = {
            "Happy/Positive": "I'm glad to hear you're feeling good!",
            "Sad/Negative": "I'm here to support you—take your time.",
            "Neutral/Mixed": "Thank you for sharing. How can I assist you further?"
        }
        return responses.get(emotion, "I’m listening.")
