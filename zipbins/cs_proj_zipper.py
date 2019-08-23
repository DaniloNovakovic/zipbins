from pathlib import Path
from zipfile import ZipFile
from .cs_proj_parser import CsProjConfig, CsProjParser


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
