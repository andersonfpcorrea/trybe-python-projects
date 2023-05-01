import pandas as pd
from src.models.dish import Dish as D
from src.models.ingredient import Ingredient as Ing


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        dataframe = pd.read_csv(source_path)
        dishes = {}
        for dish, price, ingredient, recipe_amount in dataframe.itertuples(
            index=False
        ):
            if dish not in dishes:
                dishes[dish] = D(dish, price)
            dishes[dish].add_ingredient_dependency(
                Ing(ingredient), recipe_amount
            )
        self.dishes = set(dishes.values())
