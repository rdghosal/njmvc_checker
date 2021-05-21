import yagmail
from .abstract_client import AbstractEmailClient
from .credentials import LoginCredentials
from .exceptions import ClientConnectionError

class YagmailClient(AbstractEmailClient):
    """
    Abstraction for yagmail API
    """
    def __init__(self, credentials: LoginCredentials):
        super().__init__(credentials=credentials)

    def __del__(self):
        self._instance.close()
    
    def _init_client(self, credentials: LoginCredentials):
        instance = None
        try:
            instance = yagmail.SMTP(credentials.username, \
                credentials.password)
        except:
            raise ClientConnectionError("Connection to Yagmail client failed. Check username, password, and GMail access settings.")
        return instance

    def send(self, recipients: list, subject: str, contents=str):
        try:
            self._instance.send(to=recipients
                , subject=subject, contents=contents)
        except KeyError:
            raise Exception("YagmailClient::send: Recepient and/or content not found")