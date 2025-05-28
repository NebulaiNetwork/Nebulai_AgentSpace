"""
TimeSeriesForecastingAgent
--------------------------
Forecasts future values based on time-series data using classical or ML models.
"""
&nbsp;
&nbsp;

import numpy as np
from sklearn.linear_model import LinearRegression
&nbsp;
&nbsp;

class TimeSeriesForecastingAgent:
    def __init__(self):
        self.model = LinearRegression()
        self.trained = False
&nbsp;
&nbsp;

    def train(self, X: np.ndarray, y: np.ndarray):
        self.model.fit(X, y)
        self.trained = True
        print("TimeSeriesForecastingAgent: Model trained.")
&nbsp;
&nbsp;

    def forecast(self, X_new: np.ndarray):
        if not self.trained:
            raise Exception("Model not trained yet.")
        prediction = self.model.predict(X_new)
        print(f"TimeSeriesForecastingAgent: Forecasted values {prediction}")
        return prediction
