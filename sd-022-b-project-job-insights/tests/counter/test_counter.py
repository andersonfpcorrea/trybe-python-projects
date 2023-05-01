from src.pre_built.counter import count_ocurrences


def test_counter():
    js_occ = 122
    assert count_ocurrences("data/jobs.csv", "javascript") is js_occ
