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
        "inital permit": "15"
        , "knowledge test": "17"
    }

    @staticmethod
    def get_url(self, service_name: str) -> str:
        if service_name not in self.__service_names.keys():
            return print("Invalid service name inputed.")
        page_num = self.__service_names.get(service_name)
        return self.__base_url.format(page_num)    

