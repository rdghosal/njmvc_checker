from os import getenv
from datetime import datetime
from argparse import ArgumentParser
from email_client.yagmail import YagmailClient
from scraper.selenium import SeleniumScrapper
from scraper.scaper_creator import ScraperCreator, ScraperType
from email_client.credentials import LoginCredentials
from email_client.enums import ClientType
from email_client.client_creator import EmailClientCreator
from utils import NjMvcUrlMapper, XPathAdapter


XPATH_TEMPLATE = "//div[@id='locationsDiv']/div[@class='text-capitalize'][./a[text()[contains(.,'Make Appointment')]]][./span[text()[contains(.,'{}')]]]"


class App:
    """
    This app scrapes the NJ MVC appointment portal in search for open appointments
    in one or more MVC branches.
    """
    def __get_open_cities(self, url, cities) -> list:
        count = 0
        found_cities = list()

        scraper: SeleniumScrapper = ScraperCreator().create_scraper(scraper_type=ScraperType.DYNAMIC)
        for x in XPathAdapter.generate_xpaths(template=XPATH_TEMPLATE, params=cities):
            if scraper.found_element(xpath=x, src_path=url):
                found_cities.append(cities[count])
            count += 1
        return found_cities

    def __get_email_msg(self, found_cities: list, service_name: str, url: str) -> str:
        msg = ""
        if len(found_cities) > 0:
            msg = f"Found {service_name} appointments available in the following cities:"
            bullet_pts = "\n\t- ".join(found_cities)
            msg = f"{msg}\n\t- {bullet_pts}"
            msg += f"\n\n{url}"
        return msg

    def __init_argparser(self) -> ArgumentParser:
        desc = """
                NjMvcChecker is a web scrapper that e-mails designated e-mail addresses about open appointments
                for either permits or knowledge tests in designated MVC branches.
               """
        parser = ArgumentParser(description=desc)
        parser.add_argument("-s", "--service_name", required=True \
            , help="Service name to check.")
        parser.add_argument("-c", "--cities", required=True \
            , help="List of cities (branch names) to check.")
        return parser

    def __get_args(self):
        parser = self.__init_argparser(self)
        return parser.parse_args()

    @staticmethod
    def run():
        args = App.__get_args(self=App)
        cities: list = args.cities.split(",")
        cities = [ c.strip().title() for c in cities ]

        service_name = args.service_name.strip().title()

        print("[{0}] Beginning search for {1} appointments in {2}".format(datetime.now(), service_name, ", ".join(cities)))
        print(f"[{datetime.now()}] Logging into e-mail client...")
        client: YagmailClient = EmailClientCreator().get_client(client_type=ClientType.GMAIL, \
            credentials=LoginCredentials(client_type=ClientType.GMAIL))

        url = NjMvcUrlMapper.get_url(service_name=service_name)

        print(f"[{datetime.now()}] Scrapping {url} for open appointments...")
        found_cities = App.__get_open_cities(self=App, url=url, cities=cities)
        msg = App.__get_email_msg(self=App, found_cities=found_cities, service_name=service_name, url=url)

        if msg:
            print(f"[{datetime.now()}] Found {len(found_cities)} appointments. Sending email(s)...")
            client.send(recipients=getenv("RECIPIENTS").split(",") \
                , subject=f"Found {len(found_cities)} Open Appointment(s) for MVC {service_name}"
                , contents=msg)
        else:
           print(f"[{datetime.now()}] No appointments found.") 

        print(f"[{datetime.now()}] Completed scraping of {url}.")

