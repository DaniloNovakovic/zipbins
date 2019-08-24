from dataclasses import dataclass, field
from typing import List


@dataclass
class CsProjConfig:
    root_namespace: str = ""
    assembly_name: str = ""
    output_type: str = ""
    output_paths: List[str] = field(default_factory=lambda: [])
