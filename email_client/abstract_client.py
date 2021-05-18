from abc import ABC, abstractmethod 


class AbstractEmailClient(ABC):
    """
    Base class for email client types
    """
    def __init__(self, **kwargs):
        self._instance = self._init_client(**kwargs)

    def __del__():
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "send") \
            and hasattr(subclass, "_instance")
            and callable(subclass.send) or NotImplemented)

    @abstractmethod
    def _init_client():
        NotImplementedError

    @abstractmethod
    def send() -> None:
        NotImplementedError

