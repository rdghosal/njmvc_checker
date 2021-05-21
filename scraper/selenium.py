from time import sleep
from scraper import WebScraper
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException, NoSuchAttributeException
from selenium.webdriver.chrome.options import Options


class SeleniumScrapper(WebScraper):
    """
    Web scrapper based on Selenium
    Using headless Chrome for driver
    """
    def __init__(self):
        # Reference: https://stackoverflow.com/a/53657649
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        super().__init__(webdriver.Chrome(options=chrome_options))

    def __del__(self):
        self.close()

    def find_element(self, xpath: str, src_path="", element: WebElement=None) -> WebElement:

        target_element: WebElement = None

        # src_path should only be specified if no element
        if src_path and not element:
            self._http_client.get(src_path)
        
        # Find element in page or in specified WebElement
        try:
            if element:
                target_element = element.find_element_by_xpath(xpath)
            else:
                target_element = self._http_client.find_element_by_xpath(xpath)
        except (InvalidSelectorException, NoSuchAttributeException) as e:
            print("Invalid XPath: Specified XPath was invalid. Please check XPath and try again.")
        except NoSuchElementException:
            print("Element Not Found: Specified XPath failed to locate element on webpage.")
        return target_element

    def found_element(self, xpath: str, src_path: str="", element: WebElement=None) -> bool:
        found = self.find_element(xpath=xpath, src_path=src_path, element=element) != None
        return found

    def close(self) -> None:
        self._http_client.close()
        self._http_client = None