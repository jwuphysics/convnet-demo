# Convnet Demo
## A demonstration of convnets using Pytorch + fastai


This notebook can be thought of as an introduction to my paper, Using 
three-band SDSS imaging to predict gas-phase metallicity 
[(Wu & Boada 2018)](https://arxiv.org/abs/1810.12913).


## Table of contents
- [Usage](#usage)
- [Install](#install)
- [Data](#data)

## Usage
Download this repository by running
```
git clone https://github.com/jwuphysics/convnet-demo.git
cd convnet-demo
```

## Install
Download version 0.7.0 of the [fastai](https://github.com/fastai/fastai) machine 
learning and [Pytorch](https://pytorch.org/). This can be installed 
by running the following (assuming you don't have a GPU):
```
git clone https://github.com/fastai/fastai.git
cd fastai 
conda env create -f environment-cpu.yml
```

Activate your environment and downgrade the Pytorch `torchtext` 
package (my code won't work with `torchtext>=3.0`.):

```
source activate fastai-cpu
pip install torchtext==0.2.3
```

You will also need to symlink to the fastai library into the `./notebooks`
directory (or add it to your Python `sys.path`). To do the former, simply 
do something like:
```
ln -s /path/to/fastai-git-repo/fastai ./notebooks/fastai
```

## Data
I snagged 500 random sources from the actual data set used in our paper. These
can directly be downloaded via Github since they total about 10 MB.
