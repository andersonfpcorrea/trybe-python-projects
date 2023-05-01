from datetime import datetime as dt
from inventory_report.inventory.product import Product


class SimpleReport:
    @staticmethod
    def is_older(product: Product, current_oldest: str) -> bool:
        current_oldest_date = dt.strptime(current_oldest, "%Y-%m-%d")
        product_created_at = dt.strptime(
            product["data_de_fabricacao"], "%Y-%m-%d"
        )
        return product_created_at < current_oldest_date

    @staticmethod
    def is_closer_to_expire(
        product: Product, current_closest_to_expire: str
    ) -> bool:
        current_oldest_date = dt.strptime(
            current_closest_to_expire, "%Y-%m-%d"
        )
        product_expire_date = dt.strptime(
            product["data_de_validade"], "%Y-%m-%d"
        )
        return (
            product_expire_date < current_oldest_date
            if product_expire_date > dt.today()
            else False
        )

    @staticmethod
    def find_the_company_with_more_products(companies: dict) -> str:
        company_with_more_products = ""
        count = 0
        for key in companies:
            if companies[key] > count:
                company_with_more_products = key
                count = companies[key]
        return company_with_more_products

    @staticmethod
    def generate(products_list: list[Product]) -> str:
        oldest_product = "9999-01-01"
        closest_expire_date = "9999-01-01"
        companies = {}

        for product in products_list:
            if SimpleReport.is_older(product, oldest_product):
                oldest_product = product["data_de_fabricacao"]
            if SimpleReport.is_closer_to_expire(product, closest_expire_date):
                closest_expire_date = product["data_de_validade"]
            if product["nome_da_empresa"] in companies:
                companies[product["nome_da_empresa"]] += 1
                continue
            companies[product["nome_da_empresa"]] = 1

        comp_with_more_prod = SimpleReport.find_the_company_with_more_products(
            companies
        )

        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {closest_expire_date}\n"
            f"Empresa com mais produtos: {comp_with_more_prod}"
        )
