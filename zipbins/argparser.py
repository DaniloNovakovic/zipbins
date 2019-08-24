import argparse
import os
from pathlib import Path


def _dir_path(path: str) -> Path:
    if os.path.isdir(path):
        return Path(path).resolve()
    else:
        raise argparse.ArgumentTypeError(
            f"readable_dir:{path} is not a valid path (hint: either use '/' as separator instead of '\\' or wrap path in '\"'' ")


def get_args() -> argparse.Namespace:
    ''' Parses command line arguments and returns `Namespace` wrapper containing the parsed objects'''
    parser = argparse.ArgumentParser(
        prog='zipbins',
        description='Find and zip all of the compiled csharp binaries to output location',
        epilog='Example: %(prog)s -p "c:\dev\myproj" -o "../myproj-bins.zip"')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0')
    parser.add_argument('-p', '--path', default='.', type=_dir_path,
                        help='''Path to the root folder (default: "%(default)s").
                        When entering value you should either use "/" instead of "\\" as delimiter (ex. ../dir/subdir), or wrap path in double quotes (ex. "c:\dir1\dir2")''')
    parser.add_argument('-o', '--output', default='./bins.zip', type=Path,
                        help='Path to the output location relative to the provided `--path` (default: "%(default)s")')

    return parser.parse_args()
