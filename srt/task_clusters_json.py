import json
from srt.paths import *
import fasttext
from sklearn.cluster import MiniBatchKMeans


def clusters_json():
    model = fasttext.load_model(str(out.ft_model))
    kmean = MiniBatchKMeans(
        n_clusters=118,
        random_state=2020,
    )

    labels = list(kmean.fit_predict([model[word] for word in model.words]))
    labels = [int(label) for label in labels]

    with open(out.clusters_json, 'w') as f:
        json.dump(list(zip(model.words, labels)), f)
