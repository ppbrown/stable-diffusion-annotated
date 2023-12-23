#!/usr/bin/python

# Whereas the txt2img.py script has more complicated configuration
# (primarily for use by batch scripts),
# this script is the "hey just use the public libs now" example.
# Note that this will generate a single image,
# and attempt to pop up a display prog for it when complete

model_file="model.safetensors"

# What makes this extra interesting, even beyond the 
# "old methods vs new methods" comparison, is that the other
# methods here, like txt2img.py,wont run in 4gigs of VRAM
# But this file will. See the "TUNING" section below,
# for relevant info

# For "tracing what the libraries do", see
#   https://huggingface.co/docs/diffusers/optimization/memory#tracing

import torch
from diffusers import StableDiffusionPipeline

# If you want to load things over the internet,
# using the "huggingface hub" module:
# pipe = StableDiffusionPipeline.from_pretrained(
#    "runwayml/stable-diffusion-v1-5",

pipe = StableDiffusionPipeline.from_single_file(
    model_file,
    torch_dtype=torch.float16,
    use_safetensors=True,
)
pipe = pipe.to("cuda")

prompt = "a photo of an ast ronaut riding a horse on mars"

# TUNING HERE ######

# Slower, but saves vram memory if doing large batches
#pipe.enable_vae_slicing() 

# Save a LOT of memory, for about a 25% speed hit
#pipe.enable_sequential_cpu_offload()


# If you don't enable this... it will technically still "run"
# with 4gigs of vram, but it will be at 1/8 the speed
pipe.enable_xformers_memory_efficient_attention()

""" Debugger tip: The first time, use "step into" feature of your debugger
    repeatedly until you get to StableDiffusionPipeline:__call__()
    Then you will want to read the code, and/or use normal steps, until you 
    find a part that particularly interests you.
"""
image = pipe(prompt,num_inference_steps=20).images[0]

image.show()
