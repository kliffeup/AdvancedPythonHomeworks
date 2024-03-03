import sys
from typing import Iterable, Optional, Tuple

import click


def calc_file_statistics(input_file: click.File) -> Tuple[int, int, int]:
    newline_count = -1
    word_count = 0
    byte_count = 0

    while True:
        line = input_file.readline()
        if not line:
            return newline_count, word_count, byte_count
        
        newline_count += 1
        word_count += len(line.split())
        byte_count += len(line.encode("utf-8"))


def format_stats_output(stats: Tuple[int, int, int], file_name: Optional[str] = None, align_len: int = 7) -> str:
    output = f"{stats[0]: >{align_len}} {stats[1]: >{align_len}} {stats[2]: >{align_len}}"
    if file_name is not None:
        output += f" {file_name}"
    
    output += "\n"
    return output


@click.command()
@click.argument("input_files", type=click.File(), nargs=-1)
def wc(input_files: Iterable[click.File]) -> None:
    """An analogue of the `wc` utility"""
    is_stdin_input = False
    if not input_files:
        input_files = (sys.stdin, )
        is_stdin_input = True

    files_stats = []
    
    for input_file in input_files:
        files_stats.append(calc_file_statistics(input_file))

    # prepare formatting info for output
    calc_sum_stats = lambda idx: sum([stats_[idx] for stats_ in files_stats]) 
    overall_stats = tuple(map(calc_sum_stats, range(len(files_stats[0]))))
    align_len = max(len(str(stat)) for stat in overall_stats)

    for idx, input_file in enumerate(input_files):
        if is_stdin_input:
            stats_str = format_stats_output(files_stats[idx])
        else:
            stats_str = format_stats_output(files_stats[idx], file_name=input_file.name, align_len=align_len)

        sys.stdout.write(stats_str)
    
    if len(input_files) > 1:
        sys.stdout.write(format_stats_output(overall_stats, file_name="total", align_len=align_len))
 
    sys.stdout.flush()


if __name__ == '__main__':
    wc()
