from typing import TYPE_CHECKING, Dict, Any
from src.python.dto.BaseDataTransferObject import BaseDataTransferObject

if TYPE_CHECKING:
    from src.python.database.models.TagModel import TagModel


class TagData(BaseDataTransferObject):
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name
        super().__init__()

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return super().get_all_data_by_dict()

    @staticmethod
    def delete_id_dict_key(data_object_dict: dict) -> dict:
        return super().delete_id_dict_key(data_object_dict)

    @staticmethod
    def create_object(id: int, name: str) -> "TagData":
        return TagData(id = id, name = name)

    @staticmethod
    def convert_to_model(data_object: "TagData") -> "TagModel":
        from src.python.database.models.TagModel import TagModel
        converted_dict = TagData.delete_id_dict_key(
            data_object_dict = data_object.get_all_data_by_dict()
        )

        return TagModel.create_model(**converted_dict)

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

