from abc import abstractmethod, ABC
from typing import Dict, Any


__all__ = ["BaseModel"]


class BaseModel:
    def __init__(self):
        pass

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return {key: value for key, value in self.__dict__.items()}

    @staticmethod
    def delete_model_dict_key(model_object_dict: dict) -> dict:
        for key in list(model_object_dict.keys()):
            if "model" in key or key == "_sa_instance_state":
                del model_object_dict[key]

        return model_object_dict

    @staticmethod
    @abstractmethod
    def create_model(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def convert_to_dto(model):
        pass
