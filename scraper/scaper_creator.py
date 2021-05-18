from .beautiful import BeautifulScrapper
from .selenium import SeleniumScrapper
from .requests import RequestsClient
from enum import Enum


class ScraperType(Enum):
    STATIC = 1
    DYNAMIC = 2


class ScraperCreator:
    """
    Factory for WebScraper
    """
    __instance = None
    
    def create_scraper(self, scraper_type: ScraperType):
        scraper = None
        if self.__instance:
            return self.__instance
        if scraper_type == ScraperType.STATIC:
            return BeautifulScrapper(http_client=RequestsClient())
        elif scraper_type == ScraperType.DYNAMIC:
            return SeleniumScrapper()

        