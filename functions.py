import json


from typing import List

from api_models.hh_ru_api import HhRuAPI
from api_models.super_job_api import SuperJobAPI
from classes.vacancy import Vacancy


def sj_ru_vacancies(find_key):
    """
    method for getting vacancies
    :return: list
    """
    vacancies = SuperJobAPI()
    vacancies_data = vacancies.get_jobs(find_key)

    vacancies_list = []

    for v in vacancies_data['objects']:
        title = v.get('profession')
        url = v.get('link')
        salary = {
            'from': v.get('payment_from'),
            'to': v.get('payment_to'),
            'currency': v.get('currency'),
            'gross': None
        }
        if 'client' in v and 'description' in v['client']:
            description = v['client']['description']
        else:
            description = ""
        api_url = None

        job = Vacancy(title, url, salary, description, api_url)
        vacancies_list.append(job)

    return vacancies_list


def hh_ru_vacancies(user_find_key):
    """
    method for getting vacancies
    :return: list
    """
    vacancies = HhRuAPI()
    vacancies_data = vacancies.get_jobs(user_find_key)

    vacancies_list = []

    for v in vacancies_data:
        title = v.get('name')
        url = v.get('alternate_url')
        salary = v.get('salary')
        description = v.get('description')
        url_hh = v.get('url')
        job = Vacancy(title, url, salary, description, url_hh)

        vacancies_list.append(job)

    return vacancies_list


def minimum_salary(vacancies: list, salary: int):
    """
    method for getting vacancies
    with the minimum specified salary
    :return: list
    """
    vacancies_list = []
    for v in vacancies:
        salary_to, salary_from = v.get_salary_data()
        if salary_from != "" or salary_from is None:
            salary_from = salary_from or 0

        if salary_from >= salary:
            vacancies_list.append(v)

    return vacancies_list


def add_vacancies_to_json(file_name: str, vacancies_list: List) -> None:
    """
    Method of adding vacancies
    to json file
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        data = [job.convert_object_to_dict() for job in vacancies_list]
        json.dump(data, file, ensure_ascii=False, indent=2)
