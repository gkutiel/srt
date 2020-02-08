from srt.task_ft import ft
from srt.task_data_txt import data_txt
from srt.paths import *


def task_init():
    return {
        'actions': ['mkdir -p out'],
        'file_dep': [],
        'targets': [],
        'uptodate': [],
        'verbosity': 2
    }


def task_data_txt():
    return {
        'actions': [data_txt],
        'file_dep': [
            py.task_data_txt,
            data.data_srt,
        ],
        'targets': [data.data_txt],
        'uptodate': [],
        'verbosity': 2,
    }


def task_ft():
    return {
        'actions': [ft],
        'file_dep': [
            py.task_ft,
            data.data_txt
        ],
        'targets': [out.ft],
        'uptodate': [],
        'verbosity': 2
    }


def task_dummy():
    return {
        'actions': [],
        'file_dep': [],
        'targets': [],
        'uptodate': [],
        'verbosity': 2
    }
