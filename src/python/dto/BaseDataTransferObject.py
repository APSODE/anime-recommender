from abc import abstractmethod, ABC
from typing import Dict, Any


class BaseDataTransferObject(ABC):
    def __init__(self):
        pass

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}

    @staticmethod
    def delete_id_dict_key(data_object_dict: dict) -> dict:
        for key in list(data_object_dict.keys()):
            if key == "id":
                del data_object_dict[key]

        return data_object_dict

    @staticmethod
    @abstractmethod
    def create_object(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def convert_to_model(data_object):
        pass
