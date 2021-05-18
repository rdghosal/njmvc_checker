from os import getenv
from scraper.scaper_creator import ScraperCreator, ScraperType
from scraper.beautiful import BeautifulScrapper
from scraper.selenium import SeleniumScrapper

import pytest


URL = getenv("TEST_URL") 


@pytest.fixture(scope="module")
def scraper():
    s = ScraperCreator().create_scraper(scraper_type=ScraperType.DYNAMIC)
    return s


def test_create_static_scraper():
    s = ScraperCreator().create_scraper(scraper_type=ScraperType.STATIC)
    assert type(s) is BeautifulScrapper


def test_scraper_find_element(scraper: SeleniumScrapper):
    city = "rio grande"
    xpath = f"//div[@id='locationsDiv']/div[@class='text-capitalize'][./span[text()[contains(.,'Available')]]][./span[text()='{city.title()}']]"
    assert scraper.find_element(xpath=xpath, src_path=URL) != None
    

@pytest.mark.parametrize("src_path", [URL, ""])
def test_scraper_find_subelement(scraper: SeleniumScrapper, src_path: str):
    xpath = f"//div[@id='locationsDiv']/div[@class='text-capitalize']" 
    div = scraper.find_element(xpath=xpath, src_path=URL)
    assert scraper.find_element(xpath="//span[text()[contains(.,'Available')]]", element=div) != None


def test_scraper_found_element(scraper: SeleniumScrapper):
    city = "rio grande"
    xpath = f"//div[@id='locationsDiv']/div[@class='text-capitalize'][./span[text()[contains(.,'Available')]]][./span[text()='{city.title()}']]"
    assert scraper.found_element(xpath=xpath, src_path=URL)


@pytest.mark.parametrize("src_path", [URL, ""])
def test_scraper_found_subelement(scraper: SeleniumScrapper, src_path: str):
    xpath = f"//div[@id='locationsDiv']/div[@class='text-capitalize']" 
    div = scraper.find_element(xpath=xpath, src_path=URL)
    assert scraper.found_element(xpath="//span[text()[contains(.,'Available')]]", element=div)