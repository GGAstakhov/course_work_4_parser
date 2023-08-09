import requests
from bs4 import BeautifulSoup


class Vacancy:
    """
    Job formatting class
    """
    def __init__(self, title, url, salary, description, hh_url):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description
        self.hh_url = hh_url

    def __str__(self):
        return f"{self.title} - {self.salary}"

    def salary_formatting(self):
        """
        salary formatting method
        :return: str
        """
        format_salary = ""

        if isinstance(self.salary, dict):
            salary_from = self.salary.get("from")
            salary_to = self.salary.get("to")
            salary_currency = self.salary.get("currency")
            salary_gross = None

            if salary_from:
                format_salary = f'from {salary_from}, {salary_currency}'
            elif salary_to:
                format_salary = f'to {salary_to}, {salary_currency}'
            elif salary_from and salary_to:
                format_salary = f'from {salary_from} to {salary_to}, {salary_currency}'
            else:
                format_salary = 'salary not specified'

        return format_salary

    def description_formatting(self):
        """
        formated description method
        :return: str
        """

        if self.hh_url:
            response = requests.get(self.hh_url)
            description_data = response.json()
            my_description = description_data.get("description")

            if my_description:
                my_new_format = BeautifulSoup(my_description, "html.parser")
                my_new_format_text = my_new_format.get_text()
                return my_new_format_text

        if self.description:
            return self.description

        else:
            return "Description not found"

    def valid_data(self):
        """
        the method checks class initialization
        :return: bool
        """
        if not self.title or self.url or self.salary is None or not self.description:
            return False
        else:
            return True

    def get_salary_data(self):
        """
        the method returns the salary value
        from and up to a certain amount
        :return: str
        """
        if isinstance(self.salary, dict):
            salary_from = self.salary.get("from")
            salary_to = self.salary.get("to")
            return salary_from, salary_to
        else:
            return None, None

    def convert_object_to_dict(self):
        """
        the method converts the data into a dictionary
        :return: dict
        """
        dictionary_data = {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description_formatting()
        }
        return dictionary_data

    def __le__(self, other):
        if isinstance(other, Vacancy):
            self_to_salary, self_from_salary = self.get_salary_data()
            other_to_salary, other_from_salary = other.get_salary_data()

            # converting strings to numbers
            if self_from_salary is not None and self_from_salary != "":
                self_from_salary = int(self_from_salary)
            if self_to_salary is not None and self_to_salary != "":
                self_to_salary = int(self_to_salary)
            if other_from_salary is not None and other_from_salary != "":
                other_from_salary = int(other_from_salary)
            if other_to_salary is not None and other_to_salary != "":
                other_to_salary = int(other_to_salary)

            # if the salary is not specified
            if self_from_salary is None and self_to_salary is None:
                return True
            elif other_from_salary is None and other_to_salary is None:
                return False

            # there is no 'from' field, then it is equal to 0
            self_from_salary = self_from_salary or 0
            other_from_salary = other_from_salary or 0

            # if fields 'from' and 'to' are empty
            if self_from_salary == 0 and self_to_salary == 0 and other_from_salary == 0 and other_to_salary == 0:
                return True

            # salary equality
            if self_from_salary == other_from_salary and self_to_salary == other_to_salary:
                return "Зарплаты одинаковые"

            # salary comparison
            if self_from_salary < other_from_salary:
                return True
            elif self_from_salary > other_from_salary:
                return False

            # if 'from' fields are the same - compare by 'to' fields
            if self_to_salary is None:
                return False
            elif other_to_salary is None:
                return True
            else:
                return self_to_salary <= other_to_salary

    def __ge__(self, other) -> bool:
        """
        Method for comparing vacancies by salary (greater than or equal)
        :param other:
        :return:
        """
        result = self.__le__(other)
        return result or (result == "Salaries are equal")

    def __lt__(self, other) -> bool:
        """
        Method for comparing vacancies by salary (less)
        :param other:
        :return:
        """
        result = self.__le__(other)
        if result == "Salaries are equal":
            return False
        return result

    def __gt__(self, other) -> bool:
        """
        Method for comparing vacancies by salary (more)
        :param other:
        :return:
        """
        result = self.__le__(other)
        if result == "Salaries are equal":
            return False
        return not result
