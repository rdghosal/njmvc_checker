from os import getenv
from argparse import ArgumentParser
from email_client.yagmail import YagmailClient
from scraper.selenium import SeleniumScrapper
from scraper import scaper_creator
from scraper.scaper_creator import ScraperCreator, ScraperType
from email_client.credentials import LoginCredentials
from email_client.enums import ClientType
from email_client.client_creator import EmailClientCreator
from njmvc_checker.url_mapper import NjMvcUrlMapper
from .xpath_adapter import XPathAdapter


XPATH_TEMPLATE = "//div[@id='locationsDiv']/div[@class='text-capitalize'][./a[text()[contains(.,'Make Appointment')]]][./span[text()='{}']]"


class App:
    """
    This app scrapes the NJ MVC appointment portal in search for open appointments
    in one or more MVC branches.
    """
    def __get_open_cities(self, url, cities):
        count = 0
        found_cities = list()

        for x in XPathAdapter.generate_xpaths(template=XPATH_TEMPLATE, params=cities):
            scraper: SeleniumScrapper = ScraperCreator().create_scraper(scraper_type=ScraperType.DYNAMIC)
            if scraper.found_element(xpath=x , src_path=url):
                found_cities.append(cities[count])
            count += 1
        return found_cities

    def __get_email_msg(self, found_cities):
        msg = ""
        if len(found_cities) > 0:
            msg = "Found appointments available in the following cities:"
            msg = "{msg}\n\t-.{}".format("\n\t-".join(found_cities))
        return msg

    def __init_argparser(self) -> ArgumentParser:
        desc = """
                NjMvcChecker is a web scrapper that e-mails designated e-mail addresses about open appointments
                for either permits or knowledge tests in designated MVC branches.
               """
        parser = ArgumentParser(description=desc)
        parser.add_argument("-s", "--service_name", nargs=1, required=True \
            , help="Service name to check.")
        parser.add_argument("-c", "--cities", nargs="+", required=True \
            , help="List of cities (branch names) to check.")
        return parser

    def __get_args(self):
        parser = self.__init_argparser()
        return parser.parse_args()

    @staticmethod
    def run():
        args = App.__get_args()
        cities: list = args.cities

        print("Logging into e-mail client...")
        client: YagmailClient = EmailClientCreator.get_client(client_type=ClientType.GMAIL, \
            credentials=LoginCredentials(client_type=ClientType.GMAIL))

        url = NjMvcUrlMapper.get_url(service_name=args.service_name)

        print(f"Scrapping {url} for open appointments...")
        found_cities = App.__get_open_cities(url=url, cities=cities)
        msg = App.__get_email_msg(found_cities=found_cities)

        if msg:
            print("Found appointments. Sending email(s)...")
            client.send({"recipients": getenv("RECIPIENTS") \
                , "title": f"Open Appointment Found in {len(found_cities)}" \
                , "contents": msg })
        else:
           print("No appointments found.") 

        print(f"Completed scrapping of {url}.")

