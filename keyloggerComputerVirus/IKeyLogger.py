from abc import ABC, abstractmethod
from typing import List



class IKeyLogger(ABC):
    @abstractmethod
    def start_listening(self) -> None:
        pass

    @abstractmethod
    def stop_listening(self) -> None:
        pass



