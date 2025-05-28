"""
CreativityAgent
---------------
Generates innovative and creative ideas using prompt-based language generation.
"""
&nbsp;
&nbsp;

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
&nbsp;
&nbsp;

class CreativityAgent:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.model.eval()
&nbsp;
&nbsp;

    def create_ideas(self, prompt: str, max_length: int = 100) -> str:
        """
        Generate creative text based on input prompt.
        """
        try:
            inputs = self.tokenizer.encode(prompt, return_tensors="pt")
            outputs = self.model.generate(
                inputs,
                max_length=max_length,
                do_sample=True,
                temperature=0.85,
                top_p=0.9,
                num_return_sequences=1,
                no_repeat_ngram_size=3,
            )
            generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            # Return the generated ideas following the prompt
            return generated[len(prompt):].strip()
        except Exception as e:
            return f"Error generating ideas: {e}"
