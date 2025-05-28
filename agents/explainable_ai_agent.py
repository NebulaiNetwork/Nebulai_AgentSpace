"""
ExplainableAIAgent
------------------
Provides interpretable explanations for AI model decisions to increase transparency.
"""
&nbsp;
&nbsp;

class ExplainableAIAgent:
    def __init__(self):
        pass
&nbsp;
&nbsp;

    def generate_explanation(self, model_output: dict) -> str:
        explanation = "The model predicted with confidence based on the following key factors:\n"
        for feature, importance in model_output.get("feature_importances", {}).items():
            explanation += f"- {feature}: importance {importance}\n"
        return explanation or "No explanation available."
