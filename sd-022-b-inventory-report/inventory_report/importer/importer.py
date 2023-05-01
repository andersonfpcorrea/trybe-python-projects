from abc import ABC


class Importer(ABC):
    @staticmethod
    def import_data(path: str):
        pass
