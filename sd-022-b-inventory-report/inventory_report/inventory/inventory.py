from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        if type != "simples" and type != "completo":
            return None

        if path.endswith(".csv"):
            result = CsvImporter.import_data(path)
            return (
                CompleteReport.generate(result)
                if type == "completo"
                else SimpleReport.generate(result)
            )
        if path.endswith(".json"):
            result = JsonImporter.import_data(path)
            return (
                CompleteReport.generate(result)
                if type == "completo"
                else SimpleReport.generate(result)
            )
        if path.endswith(".xml"):
            result = XmlImporter.import_data(path)
            return (
                CompleteReport.generate(result)
                if type == "completo"
                else SimpleReport.generate(result)
            )
