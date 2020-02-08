from srt.paths import *
import pandas as pd


def data_json():
    clusters = pd.read_json(out.clusters_json, lines=True)
    clusters['x'] = clusters['vec_2'].apply(
        lambda xy: xy[0]
    )
    clusters['y'] = clusters['vec_2'].apply(
        lambda xy: xy[1]
    )
    clusters.rename(columns={'word': 'data'}, inplace=True)
    clusters[['x', 'y', 'label', 'data']].to_json(
        out.data_json,
        orient='records'
    )
