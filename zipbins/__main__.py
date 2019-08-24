
from pathlib import Path
from zipfile import ZipFile
from zipbins.csproj.zipper import CsProjZipper
from zipbins.csproj.parser import CsProjParser
from zipbins.argparser import get_args


def zip_bins(root_path: Path, output_dest: Path, zipper: CsProjZipper, search_pattern="*.csproj"):
    with ZipFile(output_dest, "w") as zip:
        for proj_path in Path(root_path).rglob(search_pattern):
            zipper.zip_proj(proj_path, zip)


def main():
    args = get_args()
    root_path = Path(args.path)
    output_dest = (root_path / args.output).resolve()

    parser = CsProjParser()
    zipper = CsProjZipper(parser=parser)
    zip_bins(root_path, output_dest, zipper)

    print(f"\nFinished zipping to '{output_dest}'")


if __name__ == "__main__":
    main()
