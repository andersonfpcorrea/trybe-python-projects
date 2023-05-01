from src.pre_built.sorting import sort_by
from copy import deepcopy


def test_sort_by_criteria():
    jobs = [
        {
            "date_posted": "2023-03-01",
            "max_salary": 10,
            "min_salary": 1,
        },
        {
            "date_posted": "2023-03-02",
            "max_salary": 11,
            "min_salary": 2,
        },
        {
            "date_posted": "2023-03-03",
            "max_salary": 13,
            "min_salary": 3,
        },
    ]

    jobs_copy = []
    for job in jobs:
        jobs_copy.append(deepcopy(job))

    def sort_by_max_salary(e):
        return e["max_salary"]

    def sort_by_date(e):
        return e["date_posted"]

    sort_by(jobs_copy, "min_salary")
    assert jobs_copy == jobs

    sort_by(jobs_copy, "max_salary")
    jobs.sort(reverse=True, key=sort_by_max_salary)
    assert jobs_copy == jobs

    sort_by(jobs_copy, "date_posted")
    jobs.sort(reverse=True, key=sort_by_date)
    assert jobs_copy == jobs
