import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".csv"):
            with open(path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file, delimiter=",", quotechar='"')
                result = []
                for row in reader:
                    result.append(row)
            return result

        raise ValueError("Arquivo inválido")
