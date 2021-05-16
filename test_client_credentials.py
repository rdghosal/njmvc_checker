import pytest
from client import *
from os import getenv


# \\\\\\\\\\\\\\\\\\\\\\
#  FIXTURE DEFINITIONS
# //////////////////////

@pytest.fixture(scope="module")
def client_creator() -> EmailClientCreator:
    ct: ClientType = ClientType.GMAIL
    lc: LoginCredentials = LoginCredentials(client_type=ct)
    return EmailClientCreator().get_client(client_type=ct, \
        credentials=lc)
    
    
# \\\\\\\\\\\\\\\\\\\\\\
#  METHOD TESTS
# //////////////////////

def test_emailclientadapter_send(client_creator: EmailClientCreator):
    args: dict = {
        "recipient": getenv("RECIPIENTS").split(",")
        , "subject": "Test E-mail"
        , "contents": "This is a test email sent via Python"
    }
    client_creator.send(**args)
    