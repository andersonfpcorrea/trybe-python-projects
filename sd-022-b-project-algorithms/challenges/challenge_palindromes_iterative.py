def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not len(word):
        return False
    return word == "".join([*word[::-1]])
