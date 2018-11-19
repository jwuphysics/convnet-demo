# Convnet Demo
## A demonstration of convnets using Pytorch + fastai

This can be thought of as an introduction to my paper, "Using three-band 
SDSS imaging to predict gas-phase metallicity" [(Wu & Boada 2018)]
(https://arxiv.org/abs/1810.12913). The repository contains some 
training and testing data for which we can use convolutional neural 
networks (convnets) to predict gas-phase metallicity.

## Table of contents
- [Install](#install)
- [Usage](#usage)
- [Data](#data)

## Install

### Clone this repo

Download this repository by running
```
git clone https://github.com/jwuphysics/convnet-demo.git
cd convnet-demo
```

### fastai

Install version 0.7.0 of [fastai](https://github.com/fastai/fastai)
and the corresponding [Pytorch](https://pytorch.org/). You can do this
by executing the following (assuming you don't have a GPU):

```
conda env create -f environment-cpu.yml
conda activate fastai-cpu

pip install fastai==0.7.0
pip install torchtext==0.2.3
```

Note that if you do have a GPU, you can instead run: 
```
conda env create -f environment.yml
```

## Usage
In order to execute the Jupyter notebook(s), simply make sure you are in 
the `fastai-cpu` environment, and then serve up a Jupyter notebook.

You can then navigate to the `./notebook` directory and open whatever
notebook you want.

The notebook `Pytorch and fastai demo.ipynb` contains some information
and instructions on getting started with writing a basic Pytorch convnet.
I've also included some fastai functionality such as finding an optimal
learning rate, cyclical learning rate schedules, and data augmentation.

The notebook `Image resolution demo.ipynb` shows examples for how to 
resize images with fastai and gives examples how to make predictions 
using low-resolution images with a super simple network.

## Data
I snagged 500 random objects from the actual data set used in our paper. 
These are directly bundled in this repository since the images are small 
and they only total about 10 MB. There are 400 training images (which 
should be broken up into roughly an 320/80 training/validation split) 
and 100 test images.

If you want the full SDSS data set that we have used in the paper, please
see the [other repo](https://github.com/jwuphysics/galaxy-cnns), which 
contains instructions for querying the data.
