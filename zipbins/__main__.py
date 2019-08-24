
from pathlib import Path
from zipbins.csproj.zipper import zip_bins
from zipbins.csproj.parser import CsProjParser
from zipbins.argparser import get_args


def main():
    args = get_args()
    root_path = Path(args.path)
    output_dest = (root_path / args.output).resolve()

    parser = CsProjParser()
    zip_bins(root_path, output_dest, parser)

    print(f"\nFinished zipping to '{output_dest}'")


if __name__ == "__main__":
    main()
