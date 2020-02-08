import fasttext
from pandas import DataFrame
from sklearn.cluster import MiniBatchKMeans
from sklearn.manifold import TSNE

from srt.paths import *


def clusters_json():
    model = fasttext.load_model(str(out.ft_model))
    kmean = MiniBatchKMeans(
        n_clusters=118,
        random_state=2020,
    )

    vecs_100 = [model[word] for word in model.words]
    labels = list(kmean.fit_predict(vecs_100))

    tsne = TSNE(random_state=2020)
    vecs_2 = tsne.fit_transform(vecs_100)

    clusters = [
        {
            'words': word,
            'label': label,
            'vec_100': vec_100,
            'vec_2': vec_2,
        }

        for word, label, vec_100, vec_2 in zip(
            model.words,
            labels,
            vecs_100,
            vecs_2
        )
    ]

    DataFrame(clusters).to_json(
        out.clusters_json,
        lines=True,
        orient='records',
    )
