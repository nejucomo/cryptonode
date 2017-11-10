#!/usr/bin/env python

import os
import sys
import argparse
from pathlib2 import Path


executable = Path(sys.argv[0])


def main(args=sys.argv[1:]):
    """
    Manager multiple cryptocurrency nodes locally.
    """
    execname = os.path.basename(sys.argv[0])
    if execname == 'cryptonode':
        cryptonode_main(args)
    else:
        wrapper_main(args)


def cryptonode_main(args):
    opts = parse_args(args)
    bindir = opts.DIR / 'bin'
    for profdir in (opts.DIR / 'profiles').iterdir():
        profbindir = profdir / 'bin'
        if profbindir.is_dir():
            for binfile in profbindir.iterdir():
                if binfile.is_file() and binfile.stat().st_mode & 0100:
                    wrappername = '{}.{}'.format(profdir.name, binfile.name)
                    wrapperdest = bindir / wrappername
                    print('Creating {}'.format(wrapperdest))
                    wrapperdest.symlink_to(executable)


def wrapper_main(args):
    assert executable.is_symlink(), executable
    [profname, binname] = executable.name.split('.', 1)
    profdir = executable.parent.parent / 'profiles' / profname
    datadir = profdir / 'datadir'
    targetbin = profdir / 'bin' / binname
    fullargs = [str(targetbin), '-datadir=' + str(datadir)] + args
    os.execvp(fullargs[0], fullargs)


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)

    dirdefault = os.path.expanduser('~/.cryptonode')
    p.add_argument(
        '--dir',
        dest='DIR',
        type=Path,
        default=Path(dirdefault),
        help='Base config directory. Default: {!r}'.format(dirdefault)
    )
    return p.parse_args(args)


if __name__ == '__main__':
    main()
