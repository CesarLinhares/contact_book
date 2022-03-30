from abc import ABC, abstractmethod


class IConnection(ABC):
    connection: any

    @abstractmethod
    def get_connection(self):
        pass
