from abc import ABC, abstractmethod

from src.core.interfaces.repository.interface import IRepository


class IRedis(IRepository, ABC):
    @abstractmethod
    def verify_if_exists(self, key: str):
        pass
