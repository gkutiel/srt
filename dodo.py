from srt.srt_2_txt import srt_2_txt


def task_srt_2_txt():
    def srt_2_txt_all():
        with open('all.txt', 'w') as f:
            f.write('\n'.join(srt_2_txt('all.srt')))

    return {
        'actions': [srt_2_txt_all],
        'file_dep': [
            'srt/srt_2_txt.py',
            'all.srt',
        ],
        'targets': ['all.txt'],
        'uptodate': [],
        'verbosity': 2,
    }
