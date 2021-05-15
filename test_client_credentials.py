import pytest
from client import *
from os import getenv


# \\\\\\\\\\\\\\\\\\\\\\
#  FIXTURE DEFINITIONS
# //////////////////////

@pytest.fixture(scope="module")
def client() -> EmailClientAdapter:
    ct: ClientType = ClientType.GMAIL
    lc: LoginCredentials = LoginCredentials(client_type=ct)
    return EmailClientAdapter(client_type=ct, \
        credentials=lc)
    
    
# \\\\\\\\\\\\\\\\\\\\\\
#  METHOD TESTS
# //////////////////////

def test_emailclientadapter_send(client: EmailClientAdapter):
    args: dict = {
        "recipient": getenv("RECIPIENT")
        , "contents": "This is a test email sent via Python"
    }

    client.send(**args)
    