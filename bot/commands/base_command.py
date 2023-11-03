from abc import ABC, abstractmethod


class BaseCommand(ABC):
    def __init__(self, objects):
        self.objects = objects

    @abstractmethod
    def execute(self):
        pass
