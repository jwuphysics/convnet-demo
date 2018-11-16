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
Download this repository by running
```
git clone https://github.com/jwuphysics/convnet-demo.git
cd convnet-demo
```

Install version 0.7.0 of the [fastai](https://github.com/fastai/fastai) machine 
learning and [Pytorch](https://pytorch.org/). This can be accomplished 
by running the following (assuming you don't have a GPU):
```
git clone https://github.com/fastai/fastai.git
cd fastai 
conda env create -f environment-cpu.yml
```

Activate your environment and downgrade the Pytorch `torchtext` 
package (my code won't work with `torchtext>=0.3`.):

```
source activate fastai-cpu
pip install torchtext==0.2.3
```

You will also need to symlink to the fastai library into the `./notebook`
directory (or add it to your Python `sys.path`). To do the former, simply 
do something like:
```
ln -s /path/to/fastai-git-repo/fastai ./notebook/fastai
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
