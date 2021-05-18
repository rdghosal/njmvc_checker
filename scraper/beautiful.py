import re
from bs4 import BeautifulSoup
from scraper.scraper import WebScraper


class BeautifulScrapper(WebScraper):
    """
    Web scrapper based on BeautifulSoup
    """
    def __init__(self, http_client):
        super().__init__(http_client)
        self._soup = None
    
    def parse_response(self, src_url: str, parser_type: str):
        resp = self._http_client.send_http_get(src_url)
        self._soup = BeautifulSoup(resp, parser_type)
    
    def found_element(self, regex: re.Pattern):
        found = False
        result = self._soup.find(regex)
        if result != None:
            found = True
        return found
