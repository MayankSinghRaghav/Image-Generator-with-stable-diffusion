import torch
from diffusers import StableDiffusionPipeline
import gradio as gr

# Check CUDA availability
if not torch.cuda.is_available():
    raise EnvironmentError("CUDA is not available. Please ensure GPU drivers and torch with CUDA are installed.")

# Load the model with float16 for GPU
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16
)
pipe = pipe.to("cuda")

# Image generation function with logging
def generate_image(prompt):
    print(f"[INFO] Prompt received: {prompt}")
    if not prompt:
        return "Please enter a prompt!"
    try:
        result = pipe(prompt)
        if result and result.images:
            print("[INFO] Image generated successfully on GPU.")
            return result.images[0]
        else:
            print("[WARN] No image returned by model.")
            return "Image generation failed — empty output."
    except Exception as e:
        print(f"[ERROR] Generation failed: {e}")
        return "Image generation failed. Check logs."

# Gradio interface
gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=gr.Image(type="pil"),
    title="🎨 AI Image Generator (Stable Diffusion - GPU Optimized)",
    description="Type a creative prompt and watch an AI-generated image come to life, powered by RTX 2060!"
).launch()