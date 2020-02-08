from srt.paths import *
import fasttext


def ft_model():
    model = fasttext.train_unsupervised(
        str(data.data_txt),
        lr=0.1,
        epoch=50,
        bucket=10000,
    )

    model.save_model(str(out.ft_model))
