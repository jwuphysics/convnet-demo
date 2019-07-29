#!/home/johnwu/anaconda3/bin/python

from fastai import *
from fastai.callbacks import CSVLogger
from fastai.vision import *
from fastai.metrics import root_mean_squared_error

PATH = '/home/john/projects/convnet-demo'
rmse = root_mean_squared_error

def get_data(sz, bs, df, val_pct=0.2, seed=1234):
    """Returns a DataBunch object containing training,
    validation, and test data, based on given parameters.
    """
    tfms = get_transforms(do_flip=True,
                          flip_vert=True,
                          max_lighting=0,
                          max_warp=0
                         )

    src = (ImageItemList.from_df(df,
                                 path=PATH,
                                 folder='train',
                                 suffix='.jpg',
                                 cols='objID'
                                )
                .random_split_by_pct(val_pct, seed=seed)
                .label_from_df(cols='oh_p50', label_cls=FloatList)
          )

    data = (src.transform(tfms, size=sz)
            .databunch(bs=bs)
            .normalize()
           )

    return data

def get_learning_rate(learn, visualize=False):
    """Plots the learning rate to a temporary file."""
    lr_fname = f'{PATH}/tmp/figs/learning_rate.png'

    learn.lr_find()

    if visualize:
	    learn.recorder.plot()
	    plt.savefig(lr_fame, dpi=150)

    return

def standard_train(learn, lr, outname='train-1'):
    """Run the standard training loop and save outputs."""
    learn.fit_one_cycle(5, slice(lr*1e-2, lr))
    #learn.unfreeze()
    #learn.fit_one_cycle(10, slice(lr*1e-6, lr*1e-4))
    learn.save(outname)

if __name__ == '__main__':

    # training labels
    df = pd.read_csv(f'{PATH}/catalogs/train.csv')

    # get DataBunch object
    data = get_data(128, 16, df)

    # create learner object
    learn = create_cnn(data, arch=models.resnet18,
    	               pretrained=True, loss_func=rmse,
                       callback_fns=[CSVLogger],
                      )

    # standard training methodology (or load results)
    try:
        learn.load('train-2')
    except:
        standard_train(learn, 0.1, outname='train-1')


