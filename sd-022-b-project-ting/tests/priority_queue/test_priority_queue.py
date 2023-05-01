import pytest as p
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    q = PriorityQueue()
    data = [
        {"qtd_linhas": 6},
        {"qtd_linhas": 7},
        {"qtd_linhas": 1},
    ]
    p_data = [
        {"qtd_linhas": 1},
        {"qtd_linhas": 6},
        {"qtd_linhas": 7},
    ]

    for f in data:
        q.enqueue(f)

    for i in range(q.__len__()):
        assert q.search(i) == p_data[i]

    for f in p_data:
        assert q.dequeue() == f

    with p.raises(IndexError, match="Índice Inválido ou Inexistente"):
        q.search(0)
