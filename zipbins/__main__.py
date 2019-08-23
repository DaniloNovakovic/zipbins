import argparse
import os
import shutil
from pathlib import Path
from zipfile import ZipFile
import xml.dom.minidom
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import List


def dir_path(path: str) -> Path:
    if os.path.isdir(path):
        return Path(path).resolve()
    else:
        raise argparse.ArgumentTypeError(
            f"readable_dir:{path} is not a valid path (hint: either use '/' as separator instead of '\\' or wrap path in '\"'' ")


def get_args():
    ''' Parses command line arguments and returns `Namespace` wrapper containing the parsed objects'''
    parser = argparse.ArgumentParser(
        prog='zipbins',
        description='Find and zip all of the compiled csharp binaries to output location',
        epilog='Example: %(prog)s -p "c:\dev\myproj" -o "../myproj-bins.zip"')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0')
    parser.add_argument('-p', '--path', default='.', type=dir_path,
                        help='''Path to the root folder (default: "%(default)s").
                        When entering value you should either use "/" instead of "\\" as delimiter (ex. ../dir/subdir), or wrap path in double quotes (ex. "c:\dir1\dir2")''')
    parser.add_argument('-o', '--output', default='./bins.zip', type=Path,
                        help='Path to the output location relative to the provided `--path` (default: "%(default)s").')

    return parser.parse_args()


@dataclass
class CsProjConfig:
    rootNamespace: str = ""
    assemblyName: str = ""
    outputType: str = ""
    outputPaths: List[str] = field(default_factory=lambda: [])


class CsProjParser:
    def parse(self, path: str) -> CsProjConfig:
        namespaces = {
            'ns': 'http://schemas.microsoft.com/developer/msbuild/2003'}
        tree = ET.parse(str(path))
        root = tree.getroot()

        root_namespace = root.find(
            "ns:PropertyGroup//ns:RootNamespace", namespaces)
        assembly_name = root.find(
            'ns:PropertyGroup//ns:AssemblyName', namespaces)
        output_type = root.find(
            'ns:PropertyGroup//ns:OutputType', namespaces)

        output_paths = root.findall(
            'ns:PropertyGroup//ns:OutputPath', namespaces)
        output_paths = [op.text for op in output_paths]

        return CsProjConfig(
            rootNamespace=root_namespace.text, assemblyName=assembly_name.text,
            outputType=output_type.text, outputPaths=output_paths)


def gen_arcname(root_arcname: str, file_path: str, abs_out_path: str) -> str:
    replaced = Path(str.replace(str(file_path), str(abs_out_path), ""))
    return str(root_arcname) + str(replaced)


def zip_proj(zip: ZipFile, proj_path: Path, config: CsProjConfig):
    if not proj_path.is_dir():
        proj_path = proj_path.parent

    if config.outputType.lower() == "library":
        return

    print(f'\nZipping "{proj_path}"...')

    for out_path in config.outputPaths:
        abs_out_path = Path(proj_path.joinpath(out_path))
        root_arcname = Path(f"/{config.rootNamespace}").joinpath(out_path)
        for file_path in abs_out_path.rglob("*.*"):
            arcname = gen_arcname(root_arcname, file_path, abs_out_path)
            print(arcname)
            zip.write(file_path, arcname)


def zip_bins(root_path: Path, output_dest: Path, parser: CsProjParser, search_pattern="*.csproj"):
    with ZipFile(output_dest, "w") as zip:
        for path in Path(root_path).rglob(search_pattern):
            config = parser.parse(str(path))
            zip_proj(zip, path, config)


def main():
    args = get_args()
    root_path = args.path
    output_dest = (root_path / args.output).resolve()

    parser = CsProjParser()
    zip_bins(root_path, output_dest, parser)

    print(f"\nFinished zipping to '{output_dest}'")


if __name__ == "__main__":
    main()
