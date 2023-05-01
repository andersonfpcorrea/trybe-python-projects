from typing import Union, List, Dict
from src.insights.jobs import read
from operator import itemgetter


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    max_salary = 0
    jobs = read(path)
    for job in jobs:
        try:
            if job["max_salary"] != "" and int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])
        except ValueError:
            continue

    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    min_salary = float("inf")
    jobs = read(path)
    for job in jobs:
        try:
            if job["min_salary"] != "" and int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])
        except ValueError:
            continue

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    max_salary, min_salary = itemgetter("max_salary", "min_salary")(job)
    if (
        not str(max_salary).isnumeric()
        or not str(min_salary).isnumeric()
        or int(min_salary) > int(max_salary)
        or not str(salary).replace("-", "").isnumeric()
    ):
        raise ValueError
    return int(min_salary) <= int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            continue
    return filtered_jobs
