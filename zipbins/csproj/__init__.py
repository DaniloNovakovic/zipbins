"""A package for parsing .csproj files and zipping it's binaries"""

from zipbins.csproj.config import CsProjConfig
from zipbins.csproj.parser import CsProjParser
from zipbins.csproj.zipper import CsProjZipper


def zip_bins(root_path: str, output_dest: str, search_pattern="*.csproj"):
    from zipfile import ZipFile
    from pathlib import Path

    parser = CsProjParser()
    zipper = CsProjZipper(parser=parser)

    with ZipFile(output_dest, "w") as zip:
        for proj_path in Path(root_path).rglob(search_pattern):
            zipper.zip_proj(proj_path, zip)
