from src.jobs import read


def get_unique_job_types(path):
    unique_jobs = set()

    for job in read(path):
        unique_jobs.add(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    unique_industries = set()

    for industry in read(path):
        if industry["industry"] != "":
            unique_industries.add(industry["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    salaries = set()

    for salary in read(path):
        if salary["max_salary"].isdigit() and salary["max_salary"] != "":
            salaries.add(int(salary["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    salaries = set()

    for salary in read(path):
        if salary["min_salary"].isdigit() and salary["min_salary"] != "":
            salaries.add(int(salary["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    if ("min_salary" or "max_salary") not in job:
        raise ValueError("min_salary and max_salary doesnt exist")
    elif type(job["min_salary"] or job["max_salary"]) != int:
        raise ValueError("min_salary and max_salary must be a integer")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greather than max_salary")
    elif type(salary) != int:
        raise ValueError("salary must be an integer")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list.append(job)
        except ValueError:
            pass
    return list
