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
 
The code is a little wierd. Easiest way to run it could be as follows:
(after doing the venv setup...)

    cp scripts/txt2img.py .
    ./txt2img.py --ckpt /path/to/sd1.5-model.ckpt

Note that it wants an original .ckpt format file, so you are probably best off downloading
one of those
