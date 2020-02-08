from srt.task_data_json import data_json
from doit.tools import run_once
from srt.task_clusters_json import clusters_json
from srt.task_ft_model import ft_model
from srt.task_data_txt import data_txt
from srt.paths import *


def task_init():
    return {
        'actions': ['mkdir -p out'],
        'file_dep': [],
        'targets': [],
        'uptodate': [run_once],
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
        'actions': [ft_model],
        'file_dep': [
            py.task_ft_model,
            data.data_txt
        ],
        'targets': [out.ft_model],
        'uptodate': [],
        'verbosity': 2
    }


def task_clusters_json():
    return {
        'actions': [clusters_json],
        'file_dep': [
            py.task_clusters_json,
            out.ft_model
        ],
        'targets': [],
        'uptodate': [],
        'verbosity': 2
    }


def task_data_json():
    return {
        'actions': [data_json],
        'file_dep': [
            py.task_data_json,
            out.clusters_json,
        ],
        'targets': [out.data_json],
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
