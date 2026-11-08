# Disclosure Statement

The image `outputs/demo_01.png` in this repository is **AI-generated**. It is not a photograph or a real artwork.

- **Tool/model:** Stable Diffusion v1.5 (`stable-diffusion-v1-5/stable-diffusion-v1-5`), open weights under the CreativeML OpenRAIL-M licence
- **Library:** Hugging Face Diffusers (run on Google Colab GPU)
- **Prompt:** "A watercolor lighthouse at sunrise"
- **Negative prompt:** blurry, low quality, text, watermark
- **Settings:** 30 steps, guidance scale 7.5, seed 42 (see `config/params.json`)
- **Labelling:** a visible "AI-generated" label on the image, and metadata (`ai_generated`, `model`, `prompt`, `seed`) inside the PNG file. Check it with `python detect_label.py`.
- **Data:** No real person's face, voice or sensitive data was used.

## Use of AI assistance

AI tools helped me with code samples, configuration examples and documentation drafts. I chose the topic design and prompt, ran and tested the project myself, and I can explain every part of it.

## Limitation

Visible labels and metadata can be removed, for example by cropping, taking a screenshot or re-uploading the image. They support honest disclosure but do not prove an image is authentic.
