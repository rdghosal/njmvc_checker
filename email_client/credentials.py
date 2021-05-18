from os import getenv
from .enums import ClientType, CredentialType


class LoginCredentials():
    """
    Stores username and password for e-mail client
    """
    __username = ""
    __password = ""

    def __init__(self, client_type: ClientType):
        self.__set_credentials(client_type)        

    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password

    @classmethod
    def __set_credentials(self, client_type: ClientType):
        # Retrieves credentials from env
        if client_type == ClientType.GMAIL:
            self.__username = getenv(self.__get_varname(ClientType.GMAIL, CredentialType.USERNAME))
            self.__password = getenv(self.__get_varname(ClientType.GMAIL, CredentialType.PASSWORD))

    def __get_varname(client_type: ClientType, cred_type: CredentialType):
        # Retrieves environmental variable name depending on client and credential
        varname: str = ""
        if client_type == ClientType.GMAIL:
            if cred_type == CredentialType.USERNAME:
                varname = "GM_USR"
            elif cred_type == CredentialType.PASSWORD:
                varname = "GM_PWD"
        return varname
