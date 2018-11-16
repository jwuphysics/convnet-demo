# Convnet Demo
## A demonstration of convnets using Pytorch + fastai

This can be thought of as an introduction to my paper, "Using 
three-band SDSS imaging to predict gas-phase metallicity" 
[(Wu & Boada 2018)](https://arxiv.org/abs/1810.12913). 
The repository contains some training and testing data
for which we can use convolutional neural networks (convnets)
to predict gas-phase metallicity.

## Table of contents
- [Install](#install)
- [Usage](#usage)
- [Data](#data)

## Install

### fastai

First install version 0.7.0 of [fastai](https://github.com/fastai/fastai) 
and the corresponding [Pytorch](https://pytorch.org/). You can do this
by executing the following (assuming you don't have a GPU):
```
git clone https://github.com/fastai/fastai.git
cd fastai 
conda env create -f environment-cpu.yml
```

If you do have a GPU, you can swap out the last line for
`conda env create -f environment.yml`.

Activate your environment and downgrade the Pytorch `torchtext` 
package (my code won't work with `torchtext>=0.3`.):

```
source activate fastai-cpu
pip install torchtext==0.2.3
```

### Clone this repo

Download this repository by running
```
git clone https://github.com/jwuphysics/convnet-demo.git
cd convnet-demo
```

You will also need to symlink to the fastai library into the `./notebook`
directory (or add it to your Python `sys.path`). You can create a symlink
using the command
```
ln -s ../fastai/fastai ./notebook/fastai
```

## Usage
In order to execute the Jupyter notebook(s), simply make sure you are in the 
`fastai-cpu` environment, and then serve up a Jupyter notebook:
```
jupyter notebook
```

You can then navigate to the `./notebook` directory and open whatever
notebook you want.

## Data
I snagged 500 random sources from the actual data set used in our paper. These
are directly bundled in this repository since the images are small and they
only total about 10 MB. There are 400 training images (which should be broken
up into roughly an 320/80 training/validation split) and 100 test images.
