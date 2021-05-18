from .abstract_client import AbstractEmailClient
from .enums import ClientType
from .yagmail import YagmailClient
from .credentials import LoginCredentials

class EmailClientCreator():
    """
    Concrete factory for e-mail client
    """
    def __init__(self):
        self._instance = None

    def get_client(self, client_type: ClientType, credentials: LoginCredentials):

        client: AbstractEmailClient = None

        if self._instance is not None:
            return self._instance
            
        if client_type == ClientType.GMAIL:
            client = YagmailClient(credentials)
        return client

