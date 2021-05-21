from abc import ABC, abstractmethod

class UrlMapper(ABC):
    """
    Utility class to map a parameter to corresponding URL.
    """
    @staticmethod
    @abstractmethod
    def get_url() -> str:
        NotImplementedError


class NjMvcUrlMapper(UrlMapper):
    
    __base_url = "https://telegov.njportal.com/njmvc/AppointmentWizard/{}"

    __service_names: dict = {
        "initial permit": "15"
        , "knowledge test": "17"
    }

    @staticmethod
    def get_url(service_name: str) -> str:
        service_name = service_name.lower()
        if service_name not in NjMvcUrlMapper.__service_names.keys():
            return print("Input service name was invalid.")
        page_num = NjMvcUrlMapper.__service_names.get(service_name)
        return NjMvcUrlMapper.__base_url.format(page_num)    

