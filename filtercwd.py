"""
Echo stdin to stdout, replacing all instances of current working directory
with '.'.

Useful for things like converting long dir names in tracebacks into relative
dir names.
"""
import os
import sys


def transform(line, cwd, home):
    if len(cwd) >= len(home):
        line = line.replace(cwd, '.')
        line = line.replace(home, '~')
    else:
        line = line.replace(home, '~')
        line = line.replace(cwd, '.')
    return line


def main():

    cwd = os.path.join(os.getcwd(), '')
    if cwd.endswith(os.sep):
        cwd = cwd[:-1]

    home = os.path.expanduser('~')

    for line in sys.stdin:
        print(transform(line, cwd, home)[:-1])


if __name__ == '__main__':
    sys.exit(main())

