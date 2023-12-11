# TXT2IMG.py overview

## Purpose:

This file is intended to document4 low-level details of the command-line Stable Diffusion script, "txt2img.py"
If you dont care about that, you probably don't want to bother reading the rest of this file!

## Formatting guide
This file is an attempt to document the high(ish)-level code paths that txt2img.py takes to render an image using stable diffusion.
It is a merge of markdown language, and HTML, because
* github wont render *.html documents
* markdown doesnt give us nice neat formatting options when we want to output indented paragraphs

So, we will abuse HTML UL tag syntax. Note that unfortunately, *we cant indent the tags* like we would in a pure HTML document,
because then github/md will render the tags as code, insetad of using them as intended.

Unfortunately, this makes the document way less readable if viewed in the raw.
A semi-nice way  to handle this is to use the github web editor directly, and use the Preview button before the Commit button.

## Intention

This is intended to eventually be a semi-deep dive into how Stable Diffusion works.
At some point, this doc will be split up into separate documents, to give more details about relevant code sections.
We will be covering not just the code flow in the file "txt2img.py", but all the interesting modules it calls to, and submodules, etc.

# Code start

<UL>
<LI> *main* is of course the main entrypoint. It allows for a plethora of overrides via optional arguments. However
*there are many things that are not set via commandline args, but are in a config file*.<p>
Command-line arguments of special interest (defaults in parens):
<UL>
<LI> --prompt (a painting of a virus monster playing guitar)
<LI> --ddim_steps (50)
<LI> --n_samples (3)  # number of resulting IMAGES, not "samples", really.
<LI> --ckpt (models/ldm/stable-diffusion-v1/model.ckpt) 
<P></P>
<P></P>
</LI>
</UL>

<LI> The lower level config-file is "configs/stable-diffusion/v1-inference.yaml".<P>
At some point, we should probably
fill in a little bit of extra relevant detail about each one we list here. For now though, just point out the name.
<P>
The most interesting/important config file items are:
<UL>
<LI> <I>model.target</I>: <B>ldm.models.diffusion.ddpm.LatentDiffusion</B></LI>
<LI> <I>model.params.conditioning_key</I>: <B>crossattn</B></LI>
<LI> <I>model.params.cond_stage_key</I>: <B>"txt"</B></LI>
<LI> <I>model.params.monitor</I>: <B>val/loss_simple_ema</B><P>

<LI> <I>model.params.scheduler_config.target</I>: <B>ldm.lr_scheduler.LambdaLinearScheduler</B><P>

<LI> <I>model.params.unet_config.target</I>: <B>ldm.modules.diffusionmodules.openaimodel.UNetModel</B>
<LI> <I>model.params.unet_config.params</I>: <B>(lots of stuff here actually)</B><P>

<LI> <I>model.params.cond_stage_config.target</I>: <B>ldm.modules.encoders.modules.FrozenCLIPEmbedder</B><P>

</UL>

<LI> Eventually, more details and code flow will follow here!
</UL> 