# Convnet Demo
## A demonstration of convnets using Pytorch + fastai

This repository can be thought of as an introduction to my paper, 
["Using three-band SDSS imaging to predict gas-phase metallicity"](https://arxiv.org/abs/1810.12913). 
Here I give a demonstration of how to use the fastai and Pytorch 
libraries to train convolutional neural networks (convnets). We use the
convnets to predict gas-phase metallicity from images. 

Note that this tutorial assumes that you are using [Google Colab](https://colab.research.google.com/).

## Install

### Clone this repo

If you're using Google Colab, then open up 
[this notebook first](https://gist.github.com/jwuphysics/ae6901a26f5d2cb7100d8f89425586ed).
Follow the instructions inside, which should allow you to load
the repository (including the actual demo notebook and a small
data set) onto your remote Drive account.

You can also download this repository locally by running
```
git clone https://github.com/jwuphysics/convnet-demo.git
git checkout colab
cd convnet-demo
```

### fastai

We will need version 1.0 of [fastai](https://github.com/fastai/fastai)
and a corresponding version of [Pytorch](https://pytorch.org/). 
These should be preinstalled on Google Colab.

## Usage

Make sure that your Google Drive account is mounted, which you can do
by running:
```
from google.colab import drive
drive.mount('/content/drive')
```
and following the instructions.

Afterwards, simply run the notebook in `notebook/Metallicity prediction demo.ipynb`.

## Data
I snagged 500 random objects from the actual data set used in our paper. 
These are directly bundled in this repository since the images are small 
and they only total about 10 MB. There are 400 training images (which 
should be broken up into roughly an 320/80 training/validation split) 
and 100 test images.

If you want the full SDSS data set that we have used in the paper, please
see the [other repo](https://github.com/jwuphysics/galaxy-cnns), which 
contains instructions for querying the data.
