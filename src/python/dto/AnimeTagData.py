from typing import TYPE_CHECKING, Dict, Any
from src.python.dto.BaseDataTransferObject import BaseDataTransferObject

if TYPE_CHECKING:
    from src.python.database.models.AnimeTagModel import AnimeTagModel


class AnimeTagData(BaseDataTransferObject):
    def __init__(self, anime_id: int, tag_id: int):
        self._anime_id = anime_id
        self._tag_id = tag_id

        super().__init__()

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return super().get_all_data_by_dict()

    @staticmethod
    def delete_id_dict_key(data_object_dict: dict) -> dict:
        return super().delete_id_dict_key(data_object_dict)

    @staticmethod
    def create_object(anime_id: int, tag_id: int) -> "AnimeTagData":
        return AnimeTagData(
            anime_id = anime_id,
            tag_id = tag_id
        )

    @staticmethod
    def convert_to_model(data_object: "AnimeTagData") -> "AnimeTagModel":
        from src.python.database.models.AnimeTagModel import AnimeTagModel
        converted_dict = BaseDataTransferObject.delete_id_dict_key(
            data_object_dict = data_object.get_all_data_by_dict()
        )

        return AnimeTagModel.create_model(**converted_dict)

    @property
    def anime_id(self) -> int:
        return self._anime_id

    @property
    def tag_id(self) -> int:
        return self._tag_id

