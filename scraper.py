from abc import abstractmethod
import requests
from bs4 import BeautifulSoup

class WebScraper:
    """
    Base class for webscrapper
    """
    def __init__(self, http_client):
        self._http_client = http_client
    
    @abstractmethod
    def _get_http_response(self, src_url: str):
        NotImplementedError
    
    @abstractmethod
    def _parse_response(self, http_response):
        NotImplementedError
    
    @abstractmethod
    def _find_element(self, parsed):
        NotImplementedError

    @abstractmethod
    def find_element_in_page(self, src_url: str):
        NotImplementedError


class BeautifulScrapper(WebScraper):
    """
    Web scrapper based on BeautifulSoup
    """
    def __init__(self):
        super().__init__()
        self._soup = None

    @abstractmethod
    def _get_http_response(self, src_url: str):
        NotImplementedError
    
    @abstractmethod
    def _parse_response(self, http_response):
        NotImplementedError
    
    @abstractmethod
    def _find_element(self, parsed):
        NotImplementedError

    @abstractmethod
    def find_element_in_page(self, src_url: str):
        NotImplementedError


class RequestsClient:
    pass