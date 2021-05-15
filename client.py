from credentials import ClientType, LoginCredentials
from enum import Enum
from abc import ABC, abstractmethod, ABCMeta
from exceptions import ClientConnectionError

import yagmail


class AbstractEmailClient(ABC):
    """
    Base class for email client types
    """
    def __init__(self, **kwargs):
        self._instance = self._init_client(**kwargs)

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "send") \
            and hasattr(subclass, "_instance")
            and callable(subclass.send) or NotImplemented)

    @abstractmethod
    def _init_client(self):
        NotImplementedError

    @abstractmethod
    def send(self, **kwargs) -> None:
        NotImplementedError


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


class YagmailClient(AbstractEmailClient):
    """
    Abstraction for yagmail API
    """
    def __init__(self, credentials: LoginCredentials):
        super().__init__(credentials=credentials)
    
    def _init_client(self, credentials: LoginCredentials):
        instance = None
        try:
            instance = yagmail.SMTP(credentials.username, \
                credentials.password)
        except:
            raise ClientConnectionError("Connection to Yagmail client failed. Check username, password, and GMail access settings.")
        return instance

    def send(self, **kwargs):
        try:
            print(self._instance)
            self._instance.send(to=kwargs["recipient"], contents=kwargs["contents"])
        except KeyError:
            raise Exception("YagmailClient::send : Recepient and/or content not found")