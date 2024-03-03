import sys
from typing import Iterable

import click


def file_tail(input_file: click.File, n: int = 10) -> str:
    line_buffer = []
    while True:
        line = input_file.readline()
        if not line:
            return "".join(line_buffer)

        line_buffer.append(line)

        if len(line_buffer) > n:
            line_buffer.pop(0)
    

@click.command()
@click.argument("input_files", type=click.File(), nargs=-1)
def tail(input_files: Iterable[click.File], n: int = 10) -> None:
    """An analogue of the `tail` utility"""
    if not input_files:
        input_files = (sys.stdin, )
        n = 17
    
    for idx, input_file in enumerate(input_files):
        cur_file_tail = file_tail(input_file, n=n)

        if len(input_files) > 1:
            sys.stdout.write(f"==> {input_file.name} <==\n")
        sys.stdout.write(cur_file_tail)
        if idx != len(input_files) - 1:
            sys.stdout.write("\n")
        sys.stdout.flush()


if __name__ == '__main__':
    tail()
