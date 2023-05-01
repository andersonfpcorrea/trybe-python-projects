import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".xml"):
            with open(path, mode="r", encoding="utf-8") as file:
                xml = file.read()

            return xmltodict.parse(xml)["dataset"]["record"]
        raise ValueError("Arquivo inválido")
