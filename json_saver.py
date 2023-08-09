import json

from api_models.job_site_api import JobSaver


class JSONSaver(JobSaver):
    """
    json file formatting class
    """
    def __init__(self, filename):
        self.filename = filename

    def get_json_to_read(self):
        """
        json file read method
        :return: json
        """
        try:
            with open(self.filename, "r", encoding="UTF-8") as file:
                data = json.load(file)
        except Exception(FileNotFoundError):
            data = []
        return data

    def get_json_to_write(self, data):
        """
        json file save method
        :param data:
        :return: json
        """
        with open(self.filename, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def find_vacation(self, key):
        """
        method of searching for vacancies by keyword
        :param key:
        :return: list
        """
        my_data = self.get_json_to_read()
        vacancies_list = []

        for v in my_data:
            for item in v.values():
                if any(isinstance(item, str) and key.lower() in item.lower() for _ in key):
                    vacancies_list.append(v)
                    break
        return vacancies_list

    def add_vacation(self, vacancy):
        """
        method of adding for vacancies
        :param vacancy:
        :return:
        """
        data = self.get_json_to_read()
        data.append(vacancy.convert_object_to_dict())
        self.get_json_to_write(data)

    def delete_vacation(self, vacancy):
        """
        method for deleting vacancies by keyword
        :param vacancy:
        :return:
        """
        data = self.get_json_to_read()
        vacancies_list = []

        for v in data:
            if v != vacancy:
                vacancies_list.append(v)

        self.get_json_to_write(vacancies_list)
