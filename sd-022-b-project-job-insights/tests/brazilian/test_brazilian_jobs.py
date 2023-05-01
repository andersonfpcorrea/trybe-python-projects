from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    files = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for file in files:
        assert "title" in file.keys()
