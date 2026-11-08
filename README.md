# Synthetic Media & Generative Content

**Student:** Ansa Sultan | Diploma in Cloud Cyber Security | EduQual Level 3 | Topic 7

## Purpose

Generate a piece of synthetic image content responsibly using an open-source tool, and label it clearly as AI-generated. The project also shows one method for disclosing and checking AI-generated media.

## Tools and libraries

Python, Hugging Face Diffusers, Transformers, PyTorch, Pillow.

## Model

- **Model:** Stable Diffusion v1.5 (`stable-diffusion-v1-5/stable-diffusion-v1-5` on Hugging Face)
- **Licence:** CreativeML OpenRAIL-M (open weights with use restrictions). The MIT licence in this repo covers only my own code, not the model.

## Prompt design

All settings are stored in `config/params.json`, not in the code. Edit that file to change the prompt, seed or steps.

| Parameter | Value |
|---|---|
| Prompt | "A watercolor lighthouse at sunrise" |
| Negative prompt | blurry, low quality, text, watermark |
| Steps | 30 |
| Guidance scale | 7.5 |
| Seed | 42 |

The same seed and settings produce the same image, so the result is repeatable.

## Setup (Google Colab)

1. Open [Google Colab](https://colab.research.google.com), create a new notebook, and choose **Runtime > Change runtime type > GPU**.
2. Run these commands in separate cells:

```
!git clone https://github.com/anxa0-0sultan/synthetic-media-and-generative-content.git
%cd synthetic-media-and-generative-content
!pip install -r requirements.txt
!python generate_image.py
```

3. The first run downloads the model weights (several GB), so it can take a few minutes.
4. The labelled image is saved as `outputs/demo_01.png`.

## Disclosure and labelling

- A visible "AI-generated (Stable Diffusion v1.5)" label is drawn on the image.
- Metadata (`ai_generated`, `model`, `prompt`, `seed`) is saved inside the PNG.
- Check it by running:

```
!python detect_label.py
```

Expected output includes `ai_generated: true` and the model, prompt and seed.

- See [DISCLOSURE.md](DISCLOSURE.md) for the full statement.

## Limitations

Visible labels and PNG metadata are easy to remove, for example by cropping, taking a screenshot or re-uploading the image. They support honest disclosure but do not prove an image is authentic. Stronger provenance methods include C2PA content credentials and invisible watermarks.

## Responsible AI use

AI tools helped with code samples, configuration examples and documentation drafts. I did the concept learning, the design and prompt choices, and I can explain and defend all of it.

## Licence

Code: MIT (see `LICENSE`). Model: CreativeML OpenRAIL-M.
