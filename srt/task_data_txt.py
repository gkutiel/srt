from srt.paths import *
import re


def data_txt():
    with open(data.data_srt) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    lines = [
        line for line in lines
        if len(line) > 1 and not re.fullmatch(r'\d+', line) and not '-->' in line
    ]

    with open(data.data_txt, 'w') as f:
        f.write('\n'.join(lines))
