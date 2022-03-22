from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def register(self):
        pass


class IMongo(IRepository, ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def find_one(self):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_letter(self):
        pass


class IRedis(IRepository, ABC):
    @abstractmethod
    def verify_if_exists(self):
        pass
