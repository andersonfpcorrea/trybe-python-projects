from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest as p

dish_one = "meat"
dish_two = "cheese"
ing = "queijo mussarela"


# Req 2
def test_dish():
    d1 = Dish(dish_one, 2.0)
    d2 = Dish(dish_two, 1.0)

    d1.add_ingredient_dependency(Ingredient(ing), 100)

    with p.raises(TypeError, match="Dish price must be float."):
        Dish(dish_one, dish_one)
    with p.raises(ValueError, match="Dish price must be greater then zero."):
        Dish(dish_one, 0)

    assert d1.name == dish_one
    assert hash(d1) != hash(d2)
    assert hash(d1) == hash(d1)
    assert d1 == d1
    assert repr(d1) == "Dish('meat', R$2.00)"
    assert d1.get_restrictions() == set(
        {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    )
    assert d1.get_ingredients() == {Ingredient(ing)}
