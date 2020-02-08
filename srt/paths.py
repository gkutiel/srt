from pathlib import Path


class data:
    _ = Path('data')

    data_srt = _ / 'data.srt'
    data_txt = _ / 'data.txt'


class py:
    _ = Path('srt')

    task_data_txt = _ / 'task_data_txt.py'
    task_ft_model = _ / 'task_ft_model.py'
    task_clusters_json = _ / 'task_clusters_json.py'
    task_data_json = _ / 'task_data_json.py'


class out:
    _ = Path('out')

    ft_model = _ / 'ft.model'
    clusters_json = _ / 'clusters.json'
    data_json = _ / 'data.json'
