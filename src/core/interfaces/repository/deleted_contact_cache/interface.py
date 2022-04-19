from abc import ABC, abstractmethod

from src.core.interfaces.repository.interface import IDataBase


class IDeletedUser(IDataBase, ABC):
    @abstractmethod
    def remove_from_cache(self, _id: str):
        pass

    @abstractmethod
    def verify_if_is_cached(self, key: str):
        pass
