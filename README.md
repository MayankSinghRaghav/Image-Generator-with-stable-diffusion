# 🖼️ Image Generator with Stable Diffusion

This is a simple Gradio-based web app that generates high-quality images from text prompts using the [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) model. Optimized for GPU (like RTX 2060) to deliver fast and realistic results.

---

## 🚀 Features

- Generate images from any creative text prompt
- Powered by Stable Diffusion via Hugging Face's `diffusers` library
- Gradio UI — easy to use and share
- GPU-accelerated (supports float16 for faster inference)

---

## 🧠 Example Prompts

- "An astronaut riding a horse in a futuristic city"
- "Cyberpunk dragon flying over Tokyo at night"
- "A fantasy castle in the clouds at sunrise"

---

## 📦 Installation

1. Clone the repo:
```bash
git clone https://github.com/MayankSinghRaghav/Image-Generator-with-stable-diffusion.git
cd Image-Generator-with-stable-diffusion
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🧪 Usage

To launch the app:
```bash
python image_gen_app_gpu.py
```

The app will open in your browser at `http://127.0.0.1:7860`

---

## ⚡ GPU Support

Ensure PyTorch is installed with CUDA support:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

## 🛑 Note

Make sure to **exclude the `venv/` folder** by using `.gitignore`.

---

## 📄 License

This project is open-source under the MIT License.
