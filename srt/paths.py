from pathlib import Path


class py:
    _ = Path('srt')

    task_data_txt = _ / 'task_data_txt.py'
    task_ft = _ / 'task_ft.py'


class data:
    _ = Path('data')

    data_srt = _ / 'data.srt'
    data_txt = _ / 'data.txt'


class out:
    _ = Path('out')

    ft = _ / 'ft.model'
