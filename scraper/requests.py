import requests

class RequestsClient:
    """
    Wrapper for requests library
    """
    def __init__(self):
        self.__instance = requests
    
    def send_http_get(self, src_url: str):
        return self.__instance.get(src_url) 

