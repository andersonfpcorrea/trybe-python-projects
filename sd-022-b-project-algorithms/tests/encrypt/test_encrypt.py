from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(None, 1)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("None", "B")

    assert encrypt_message("123456", 99) == "654321"

    assert encrypt_message("123456", 4) == "65_4321"

    assert encrypt_message("123456", 3) == "321_654"
