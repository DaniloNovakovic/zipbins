from pathlib import Path
from zipfile import ZipFile
from zipbins.csproj.parser import CsProjParser
from zipbins.csproj.config import CsProjConfig


def _gen_arcname(root_arcname: str, file_path: str, abs_out_path: str) -> str:
    replaced = Path(str.replace(str(file_path), str(abs_out_path), ""))
    return str(root_arcname) + str(replaced)


class CsProjZipper:
    def __init__(self, parser: CsProjParser):
        self.parser = parser

    def zip_proj(self, proj_path: Path, zip: ZipFile):
        config = self.parser.parse(str(proj_path))

        if not proj_path.is_dir():
            proj_path = proj_path.parent

        if config.output_type.lower() == "library":
            return

        print(f'\nZipping "{proj_path}"...')

        for out_path in config.output_paths:
            abs_out_path = Path(proj_path.joinpath(out_path))
            root_arcname = Path(f"/{config.root_namespace}").joinpath(out_path)
            for file_path in abs_out_path.rglob("*.*"):
                arcname = _gen_arcname(root_arcname, file_path, abs_out_path)
                print(arcname)
                zip.write(file_path, arcname)
