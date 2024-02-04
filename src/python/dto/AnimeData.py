from typing import TYPE_CHECKING, Dict, Any
from src.python.dto.BaseDataTransferObject import BaseDataTransferObject

if TYPE_CHECKING:
    from src.python.database.models.AnimeModel import AnimeModel


class AnimeData(BaseDataTransferObject):

    def __init__(self, id: int, title: str, description: str):
        self._id = id
        self._title = title
        self._description = description

        super().__init__()

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return super().get_all_data_by_dict()

    @staticmethod
    def delete_id_dict_key(data_object_dict: dict) -> dict:
        return super().delete_id_dict_key(data_object_dict)

    @staticmethod
    def create_object(id: int, title: str, description: str) -> "AnimeData":
        return AnimeData(
            id = id,
            title = title,
            description = description
        )

    @staticmethod
    def convert_to_model(data_object: "AnimeData") -> "AnimeModel":
        from src.python.database.models.AnimeModel import AnimeModel
        converted_dict = AnimeData.delete_id_dict_key(
            data_object_dict = data_object.get_all_data_by_dict()
        )

        return AnimeModel.create_model(**converted_dict)

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

