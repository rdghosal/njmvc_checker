import pytest
from njmvc_checker.app import App, NjMvcUrlMapper


def test_get_email_msg(cities=["rio grande", "RAHWAY", "treNTon", "south PlainfielD", "123456"]):
    cities = [ c.title() for c in cities ]
    print(App._App__get_email_msg(self=App, found_cities=cities))


def test_url_mapper():
    url = print(NjMvcUrlMapper.get_url(service_name="PERMIT"))
    assert url == None


def test_get_open_cities(url="", cities=["rio grande", "south plainfield", "rahway"]):
    url = NjMvcUrlMapper.get_url(service_name="knowledge test")
    print(url)
    cities = [ c.title() for c in cities ]

    assert len(App._App__get_open_cities(self=App, url=url, cities=cities)) > 0

    
@pytest.mark.parametrize("cities", [[], ["Newark"], ["Rio Grande", "Rahway"]])
def test_get_email_msg(cities):
    print(App._App__get_email_msg(self=App,found_cities=cities))