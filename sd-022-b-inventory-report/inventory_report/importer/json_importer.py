import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".json"):
            with open(path, mode="r", encoding="utf-8") as file:
                return json.load(file)

        raise ValueError("Arquivo inválido")
