from credentials import ClientType, LoginCredentials
from enum import Enum
from abc import ABC, abstractmethod
from exceptions import ClientConnectionError

import yagmail


class BaseClient(ABC):
    __instance = None

    def __init__(self):
        self.__instance = None

    @abstractmethod
    def send():
        pass


class EmailClientAdapter(BaseClient):
    """
    Singleton class for e-mail client
    from https://en.wikipedia.org/wiki/Singleton_pattern
    """

    __instance = None

    def __new__(cls, client_type: ClientType, credentials: LoginCredentials):
        if cls.__instance is None:
            cls.__instance = cls.__create_client(client_type, credentials)
        return cls.__instance

    @classmethod
    def __create_client(cls, client_type: ClientType, credentials: LoginCredentials):
        eca: EmailClientAdapter = None
        if client_type == ClientType.GMAIL:
            eca = YagmailClient(credentials)

        return eca

    def send(self, **kwargs):
        self.__instance.send(kwargs)


class YagmailClient(BaseClient):
    """
    Adapter for yagmail API
    """
    def __init__(self, credentials: LoginCredentials):
        self.__instance = self.__init_yagmail(credentials)
    
    def __init_yagmail(self, credentials: LoginCredentials):
        instance = None
        try:
            instance = yagmail.SMTP(credentials.username, credentials.password)
        except:
            raise ClientConnectionError("Connection to Yagmail client failed. Check username, password, and GMail access settings.")
        return instance

    def send(self, **kwargs):
        try:
            print(kwargs)
            self.__instance.send(to=kwargs["recipient"], contents=kwargs["content"])
        except KeyError:
            raise Exception("YagmailClient::send : Recepient and/or content not found")
