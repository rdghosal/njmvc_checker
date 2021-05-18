import requests
from abc import abstractmethod


class WebScraper:
    """
    Base class for webscrapper
    """
    def __init__(self, http_client):
        self._http_client = http_client
    
    @abstractmethod
    def parse_response():
        pass
    
    @abstractmethod
    def find_element():
        pass

    @abstractmethod
    def found_element() -> bool:
        pass



