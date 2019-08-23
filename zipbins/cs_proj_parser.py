import xml.dom.minidom
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import List


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
