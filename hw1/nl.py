import sys

import click


@click.command()
@click.argument("input_file", type=click.File(), default=sys.stdin)
def nl(input_file: click.File) -> None:
    """An analogue of the `nl -b a` utility"""
    line_count = 1

    while True:
        line = input_file.readline()
        if not line:
            # sys.stdout.write("\n")
            break

        sys.stdout.write(f"{line_count: >6}\t{line}")
        sys.stdout.flush()
        line_count += 1


if __name__ == '__main__':
    nl()
