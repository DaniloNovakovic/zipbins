from dataclasses import dataclass
from pathlib import Path


@dataclass
class ZipBinsOptions:
    root_path: Path
    output_dest: Path

    def __post_init__(self):
        if not self.output_dest.is_absolute():
            self.output_dest = (self.root_path / self.output_dest).resolve()
