import requests

from api_models.job_site_api import JobSiteAPI


class SuperJobAPI(JobSiteAPI):
    """
    API class for superjob.ru
    """

    def __init__(self):
        self.url = f"https://api.superjob.ru/2.0/vacancies/"

    def connect(self):
        """
        API connection method using keys
        :return: json
        """
        print("Connecting to SuperJob.ru API")
        headers = {"X-Api-App-Id": "v3.r.137737074.c20344c5b0c109c1db3368d3d7c3ead3b13b46b8.47a2961ab0a5b10c361c3003ce0facb4182ba507"}
        response = requests.get(self.url, headers=headers)
        return response.json()

    def get_jobs(self, query):
        """
        Method for obtaining data on vacancies
        :param query:
        :return: dict
        """
        data_vacancies = self.connect()
        vacancies_list = []

        for v in data_vacancies['objects']:
            profession = v.get("profession", '').lower()
            if query.lower() in profession:
                vacancies_list.append(v)

        if not vacancies_list:
            return "Data not found"

        return {'objects': vacancies_list}
