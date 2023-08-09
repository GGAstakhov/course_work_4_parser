from abc import ABC, abstractmethod


class JobSiteAPI(ABC):
    """
    API class.


    """
    @abstractmethod
    def connect(self):
        """
        API connection method using keys
        :return: None
        """
        pass

    @abstractmethod
    def get_jobs(self, query):
        """
        Method for obtaining data on vacancies
        :param query:
        :return:None
        """
        pass


class JobSaver(ABC):
    @abstractmethod
    def find_vacation(self, key):
        """
        method of parsing vacancies, adding and deleting
        :param key:
        :return: None
        """
        pass

    @abstractmethod
    def add_vacation(self, vacancy):
        """
         method of adding vacancies
        :param vacancy:
        :return: None
        """
        pass

    @abstractmethod
    def delete_vacation(self, vacancy):
        """
        method of deleting vacancies
        :param vacancy:
        :return: None
        """
        pass
