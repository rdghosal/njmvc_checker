from os import getenv
from email_client.yagmail import YagmailClient
from scraper.selenium import SeleniumScrapper
from scraper import scaper_creator
from scraper.scaper_creator import ScraperCreator, ScraperType
from email_client.credentials import LoginCredentials
from email_client.enums import ClientType
from template_adapter import TemplateAdapter
from email_client.client_creator import EmailClientCreator

BASE_URL = "https://telegov.njportal.com/njmvc/AppointmentWizard/{}"
XPATH_TEMPLATE = "//div[@id='locationsDiv']/div[@class='text-capitalize'][./span[text()[contains(.,'Available')]]][./span[text()='{}']]"


class App:

    def _get_open_cities(self, url, cities):
        count = 0
        found_cities = list()

        for x in TemplateAdapter.get_formatted_strs(template=XPATH_TEMPLATE, params=cities):
            scraper: SeleniumScrapper = ScraperCreator().create_scraper(scraper_type=ScraperType.DYNAMIC)

            if scraper.found_element(xpath=x , src_path=url):
                found_cities.append(cities[count])
            
            count += 1

        return found_cities

    def _get_email_msg(found_cities):
        msg = ""
        if len(found_cities) > 0:
            msg = "Found appointments available in the following cities:"
            msg = "{msg}\n\t.{}".format("\n\t".join(found_cities))

        return msg

    def run(self, **kwargs):
        cities = kwargs["cities"]
        cities = cities.split(",")
        cities = [ c.title() for c in cities ]

        print("Logging into e-mail client...")
        client: YagmailClient = EmailClientCreator.get_client(client_type=ClientType.GMAIL, \
            credentials=LoginCredentials(client_type=ClientType.GMAIL))

        url = list(TemplateAdapter.get_formatted_strs(template=BASE_URL, params=["15"]))[0]

        print(f"Scrapping {url} for open appointments...")
        found_cities = self._get_open_cities(url)
        msg = self._get_email_msg(found_cities)

        if msg:
            print("Found appointments. Sending email(s)...")
            client.send({"recipients": getenv("RECIPIENTS") \
                , "title": f"Open Appointment Found in {len(found_cities)}" \
                , "contents": msg })
        else:
           print("No appointments found.") 

        print(f"Completed scrapping of {url}.")


if __name__ == "__main__":

    # todo    
    params = {
        "cities": "",
        "page": ""
    }

    App().run()