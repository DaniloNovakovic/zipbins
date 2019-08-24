import xml.dom.minidom
import xml.etree.ElementTree as ET
from zipbins.csproj.config import CsProjConfig


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
            root_namespace=root_namespace.text, assembly_name=assembly_name.text,
            output_type=output_type.text, output_paths=output_paths)
