import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        m_dict = {
            "dish_name": [],
            "ingredients": [],
            "price": [],
            "restrictions": [],
        }
        for d in self.menu_data.dishes:
            in_stk = InventoryMapping.check_recipe_availability(
                self.inventory, d.recipe
            )
            if restriction not in d.get_restrictions() and in_stk:
                m_dict["dish_name"].append(d.name)
                m_dict["ingredients"].append(d.get_ingredients())
                m_dict["price"].append(d.price)
                m_dict["restrictions"].append(d.get_restrictions())
        return pd.DataFrame(m_dict)
