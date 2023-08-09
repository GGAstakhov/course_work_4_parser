import requests

from api_models.job_site_api import JobSiteAPI


class HhRuAPI(JobSiteAPI):
    """
    API class for hh.ru
    """
    def connect(self):
        """
        API connection method using keys
        :return:
        """
        print("Connecting to HH.ru API")
        url = "https://api.hh.ru/vacancies"

        headers = {
            "User-Agent": "Your User Agent",
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items")
            return vacancies

        else:
            print(f'Ошибка {response.status_code}')

    def get_jobs(self, query):
        """
        Method for obtaining data on vacancies
        :param query:
        :return: dict
        """
        url = f"https://api.hh.ru/vacancies?text={query}"
        response = requests.get(url)
        if response.status_code == 200:
            request_data = response.json()
            jobs = request_data.get("items", [])
            if not jobs:
                return "Invalid request"
            return jobs
        else:

            return response.status_code
