# Synthetic Media & Generative Content

**Student:** Ansa Sultan | Diploma in Cloud Cyber Security | EduQual Level 3 | Topic 7

## Purpose
Generate a piece of synthetic image content responsibly using an open-source tool, and label it clearly as AI-generated.

## Setup
1. Open Google Colab and select a GPU runtime.
2. Clone this repo and run `pip install -r requirements.txt`.
3. Run `python generate_image.py`.

## Tools and libraries
Python, Hugging Face Diffusers, Transformers, PyTorch, Pillow.

## Model
Stable Diffusion v1.5 (open-source).

## Prompt design
"A watercolor lighthouse at sunrise". The negative prompt removes blur, text and watermarks. Settings: 30 steps, guidance scale 7.5, seed 42 (repeatable).

## Disclosure and labelling
- A visible "AI-generated" label is drawn on the image.
- Metadata (ai_generated, model, prompt, seed) is saved inside the PNG.
- Check it with `python detect_label.py`.
- See DISCLOSURE.md for the full statement.
