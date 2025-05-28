"""
AnomalyDetectionAgent
--------------------
Detects anomalies and outliers in data streams using statistical and ML methods.
"""
&nbsp;
&nbsp;

import numpy as np
from sklearn.ensemble import IsolationForest
&nbsp;
&nbsp;

class AnomalyDetectionAgent:
    def __init__(self):
        self.model = IsolationForest(contamination=0.01)
&nbsp;
&nbsp;

    def fit(self, data):
        """Train the model with historical data."""
        self.model.fit(data)
&nbsp;
&nbsp;

    def detect(self, data_point):
        """Return True if data_point is an anomaly, else False."""
        prediction = self.model.predict([data_point])
        return prediction[0] == -1
&nbsp;
&nbsp;

    def predict_batch(self, data_batch):
        """Detect anomalies in batch data."""
        return self.model.predict(data_batch)
