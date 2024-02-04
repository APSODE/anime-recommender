from typing import TYPE_CHECKING, Dict, Any
from src.python.dto.BaseDataTransferObject import BaseDataTransferObject

if TYPE_CHECKING:
    from src.python.database.models.TagWeightModel import TagWeightModel


class TagWeightData(BaseDataTransferObject):
    def __init__(self, user_id: int, tag_id: int, weight: int):
        self._user_id = user_id
        self._tag_id = tag_id
        self._weight = weight
        super().__init__()

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return super().get_all_data_by_dict()

    @staticmethod
    def delete_id_dict_key(data_object_dict: dict) -> dict:
        return super().delete_id_dict_key(data_object_dict)

    @staticmethod
    def create_object(user_id: int, tag_id: int, weight: int) -> "TagWeightData":
        return TagWeightData(
            user_id = user_id,
            tag_id = tag_id,
            weight = weight
        )

    @staticmethod
    def convert_to_model(data_object: "TagWeightData") -> "TagWeightModel":
        from src.python.database.models.TagWeightModel import TagWeightModel
        converted_dict = TagWeightData.delete_id_dict_key(
            data_object_dict = data_object.get_all_data_by_dict()
        )

        return TagWeightModel.create_model(**converted_dict)

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def tag_id(self) -> int:
        return self._tag_id

    @property
    def weight(self) -> int:
        return self._weight

