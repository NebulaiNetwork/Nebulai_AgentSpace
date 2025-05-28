"""
ZeroShotLearningAgent
---------------------
Performs classification on unseen classes by leveraging semantic attributes.
"""
&nbsp;
&nbsp;

from transformers import pipeline
&nbsp;
&nbsp;

class ZeroShotLearningAgent:
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification")
&nbsp;
&nbsp;

    def classify(self, sequence: str, candidate_labels: list):
        return self.classifier(sequence, candidate_labels)
