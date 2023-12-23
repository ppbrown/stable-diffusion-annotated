# Stable Diffusion Annotated

This is a fork of stable diffusion v1.5, aka
https://github.com/runwayml/stable-diffusion/

I'm not looking to modify behavior. I'm just trying to make it more comprehensible, by
adding more comments, and maybe renaming a few internal variables for readability purposes.

People who already understand and are familiar with the code are welcome to commit PRs to help in this effort.
All submissions will be personallly reviewed by me, and may be pushed back if I believe there
are readability issues.

My credentials for this, are that I've been in the industry for 30 years, and as the rest of my repos 
hopefully demonstrate, I know how to create readable code and documentation ;-) 

To ease the burden of code review, please try to submit PRs in readable chunks. 
That is to say, dont submit a PR with 1,000 lines of new comments and code. Group it into relevant chunks, please!

## Places to start

If you are interested in looking at the stable diffusion code, but dont know where to start, you might find the best place for you
by looking in the [scripts](scripts/) directory. In there, you will find starting points such as [txt2img.py](scripts/txt2img.py) and [img2img.py](scripts/img2img.py)

Of additional interest, may be
[pipeline_comparison.py](scripts/pipeline_comparison.py),
a wrapper around the modern day diffusion libraries. It runs a lot faster, but may
be more difficult to understand the internals


## OS requirements

Sorry, but the rest of these instructions are written with Linux in mind.
The stuff should work on windows, but I dont want to write two setup guides at present.
Note that you can always install WSL Ubuntu if you want the linux experience on windows, and it works for this.

## Dependancies

To install required python dependencies, it is typical to run

    pip install -r requirements.txt

NOTE HOWEVER, that it is best practice to install it in "venv", and in fact,
certain OSs like Ubuntu23 now require it!

Full instructions would be:

    sudo apt install python3-pip python3-venv # one time ever
    python -m venv venv                       # one time ever
    . venv/bin/activate

This will make your prompt start with "(venv)". Any time you want to run things in here,
you will need to be in that state

## Running txt2img.py

(Note that you will require "over 4 gigs of VRAM" to do this. 6 gigs is fine)
If you havent downloaded any models, etc. you will also need approximately 7 gigs of extra disk space.

(after doing the venv setup...)
You can call the txt2img.py script from anywhere; However, it will RUN
from the top level of this repo, and write things under the "outputs" directory
in the top level, by default

    python scripts/txt2img.py --ckpt /path/to/sd1.5-model.ckpt

The original version wanted .ckpt format file, but it has been slightly updated
to accept .safetensors format files as well. You must keep the name ending with ".safetensor"


If you want to set the original sd1.5 checkpoint (or some other one)
as the default, so you dont have to use the --ckpt arg, you can do the following:

    mkdir -p models/ldm/stable-diffusion-v1
    cd models/ldm/stable-diffusion-v1
    wget https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt
    ln -s v1-5-pruned-emaonly.ckpt model.ckpt

Note1: the original one is 4G. if you would like to use a 2G model file, you can get one from 
https://civitai.com/models/6174?modelVersionId=11047

Note2: If you want to use a model in safetensor format, the name must end in ".safetensor". Therefore, if you want that one to be default, you will have to edit the script to change the value of 'default_model_path'
