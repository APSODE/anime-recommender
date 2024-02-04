from typing import TYPE_CHECKING, Dict, Any
from src.python.dto.BaseDataTransferObject import BaseDataTransferObject

if TYPE_CHECKING:
    from src.python.database.models.UserModel import UserModel


class UserData(BaseDataTransferObject):
    def __init__(self, id: int, account_id: int, account_pw: int):
        self._id = id
        self._account_id = account_id
        self._account_pw = account_pw
        super().__init__()

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return super().get_all_data_by_dict()

    @staticmethod
    def delete_id_dict_key(data_object_dict: dict) -> dict:
        return super().delete_id_dict_key(data_object_dict)

    @staticmethod
    def create_object(id: int, account_id: int, account_pw: int) -> "UserData":
        return UserData(
            id = id,
            account_id = account_id,
            account_pw = account_pw
        )

    @staticmethod
    def convert_to_model(data_object):
        from src.python.database.models.UserModel import UserModel
        converted_dict = UserData.delete_id_dict_key(
            data_object_dict = data_object.get_all_data_by_dict()
        )

        return UserModel.create_model(**converted_dict)

    @property
    def id(self) -> int:
        return self._id

    @property
    def account_id(self) -> int:
        return self._account_id

    @property
    def account_pw(self) -> int:
        return self._account_pw

