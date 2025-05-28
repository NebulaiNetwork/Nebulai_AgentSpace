"""
SentimentAnalysisAgent
----------------------
Classifies text according to sentiment polarity and subjectivity.
"""
&nbsp;
&nbsp;

from textblob import TextBlob
&nbsp;
&nbsp;

class SentimentAnalysisAgent:
    def __init__(self):
        pass
&nbsp;
&nbsp;

    def analyze_sentiment(self, text: str):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        print(f"SentimentAnalysisAgent: Polarity={polarity:.2f}, Subjectivity={subjectivity:.2f}")
        return polarity, subjectivity
