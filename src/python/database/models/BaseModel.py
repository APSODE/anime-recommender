from abc import abstractmethod, ABC
from typing import Dict, Any


__all__ = ["BaseModel"]


class BaseModel:
    def __init__(self):
        pass

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return {key: value for key, value in self.__dict__.items()}

    @staticmethod
    @abstractmethod
    def create_model(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def convert_to_dto(model):
        pass
