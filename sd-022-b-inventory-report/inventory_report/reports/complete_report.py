from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.product import Product


class CompleteReport(SimpleReport):
    @staticmethod
    def gen_product_by_company_str_report(report: dict) -> str:
        str_report = "\nProdutos estocados por empresa:\n"

        for key in report:
            str_report += f"- {key}: {report[key]}\n"

        return str_report

    @staticmethod
    def products_by_company(data: list[Product]) -> str:
        report = {}

        for datum in data:
            if datum["nome_da_empresa"] in report:
                report[datum["nome_da_empresa"]] += 1
                continue
            report[datum["nome_da_empresa"]] = 1

        str_report = CompleteReport.gen_product_by_company_str_report(report)

        return str_report

    @staticmethod
    def generate(products_list: list[Product]) -> str:
        simple_resport = SimpleReport.generate(products_list)
        return simple_resport + CompleteReport.products_by_company(
            products_list
        )
