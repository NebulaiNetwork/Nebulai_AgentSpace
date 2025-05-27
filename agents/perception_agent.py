"""
PerceptionAgent
---------------
Processes and fuses multi-modal data (e.g., text, image) to enrich understanding.
"""
&nbsp;
&nbsp;

from PIL import Image
import io
&nbsp;
&nbsp;

class PerceptionAgent:
    def __init__(self):
        pass
&nbsp;
&nbsp;

    def process_text(self, text: str) -> str:
        # Simple text processing placeholder
        return text.lower()
&nbsp;
&nbsp;

    def process_image(self, image_bytes: bytes) -> str:
        try:
            image = Image.open(io.BytesIO(image_bytes))
            # Example: get image size for understanding
            width, height = image.size
            return f"Processed image with dimensions: {width}x{height}"
        except Exception as e:
            return f"Error processing image: {e}"
&nbsp;
&nbsp;

    def fuse_modalities(self, text: str, image_bytes: bytes) -> str:
        text_processed = self.process_text(text)
        image_processed = self.process_image(image_bytes)
        return f"Fused Modalities:\nText: {text_processed}\nImage info: {image_processed}"
