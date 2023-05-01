from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    apple = Ingredient("apple")
    orange = Ingredient("orange")
    apple_clone = Ingredient("apple")
    bacon = Ingredient("bacon")
    assert apple != orange
    assert apple == apple_clone
    assert apple.name == "apple"
    assert hash(apple) == hash(apple_clone)
    assert hash(apple) != hash(orange)
    assert repr(apple) == "Ingredient('apple')"
    assert repr(apple) != "Ingredient('orange')"
    assert len(bacon.restrictions) == 2
