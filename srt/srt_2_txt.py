import re


def srt_2_txt(srt: str):
    with open(srt) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return [
        line for line in lines
        if len(line) > 1 and not re.fullmatch(r'\d+', line) and not '-->' in line
    ]
