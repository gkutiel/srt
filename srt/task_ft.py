import fasttext


def ft():
    model = fasttext.train_unsupervised('all.txt')
    model.save_model()
