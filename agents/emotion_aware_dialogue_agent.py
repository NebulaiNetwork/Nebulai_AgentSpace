"""
EmotionAwareDialogueAgent
-------------------------
Manages dialogues considering emotional context for empathetic and effective interaction.
"""
&nbsp;
&nbsp;

from textblob import TextBlob
&nbsp;
&nbsp;

class EmotionAwareDialogueAgent:
    def __init__(self):
        pass
&nbsp;
&nbsp;

    def detect_emotion(self, text: str):
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.5:
            return "happy"
        elif polarity  -0.5:
            return "sad"
        else:
            return "neutral"
&nbsp;
&nbsp;

    def respond(self, input_text: str):
        emotion = self.detect_emotion(input_text)
        responses = {
            "happy": "I'm glad you're feeling good!",
            "sad": "I'm here if you want to talk about it.",
            "neutral": "How can I assist you today?"
        }
        return responses.get(emotion, "Tell me more.")
