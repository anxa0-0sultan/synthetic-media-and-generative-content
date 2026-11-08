import json
import torch
from PIL import ImageDraw, PngImagePlugin
from diffusers import StableDiffusionPipeline

# 1. Load settings
cfg = json.load(open("config/params.json"))

# 2. Load the open-source model (GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32
pipe = StableDiffusionPipeline.from_pretrained(
    cfg["model"], torch_dtype=dtype).to(device)

# 3. Generate the image (same seed = same image)
gen = torch.Generator(device).manual_seed(cfg["seed"])
image = pipe(
    cfg["prompt"],
    negative_prompt=cfg["negative_prompt"],
    num_inference_steps=cfg["steps"],
    guidance_scale=cfg["guidance_scale"],
    generator=gen,
).images[0]

# 4. Disclose: visible label on the image
label = "AI-generated (Stable Diffusion v1.5)"
draw = ImageDraw.Draw(image)
draw.rectangle([0, image.height - 30, image.width, image.height], fill=(0, 0, 0))
draw.text((10, image.height - 22), label, fill=(255, 255, 255))

# 5. Disclose: metadata saved inside the file
meta = PngImagePlugin.PngInfo()
meta.add_text("ai_generated", "true")
meta.add_text("model", "Stable Diffusion v1.5")
meta.add_text("prompt", cfg["prompt"])
meta.add_text("seed", str(cfg["seed"]))
image.save("outputs/demo_01.png", pnginfo=meta)
print("Saved outputs/demo_01.png")
