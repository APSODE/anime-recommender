from typing import TYPE_CHECKING, Dict, Any

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.python.database.DatabaseCreator import DatabaseCreator
from src.python.database.models.BaseModel import BaseModel

if TYPE_CHECKING:
    from src.python.dto.UserData import UserData

_BACK_POPULATES_PARAMS = "user_model"


class UserModel(BaseModel, DatabaseCreator.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    account_id = Column(String(255), nullable = False)
    account_pw = Column(String(255), nullable = False)  # 해시를 이용해 암호화된 비밀번호를 저장할 예정

    # relationship 정의 과정에서 순환참조 문제가 발생하는 것을 해결하기 위해
    # 모델 클래스를 문자열을 사용해 지정하는 것이 아닌 직접 클래스를 이용해 지정하였음
    from src.python.database.models.TagWeightModel import TagWeightModel
    tag_weight_model = relationship(
        TagWeightModel,
        back_populates = _BACK_POPULATES_PARAMS
    )

    def __init__(self, account_id: str, account_pw: str):
        self.account_id = account_id
        self.account_pw = account_pw
        super().__init__()

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return super().get_all_data_by_dict()

    @staticmethod
    def create_model(account_id: str, account_pw: str) -> "UserModel":
        return UserModel(account_id = account_id, account_pw = account_pw)

    @staticmethod
    def convert_to_dto(model: "UserModel") -> "UserData":
        from src.python.dto.UserData import UserData
        converted_dict = BaseModel.delete_model_dict_key(
            model_object_dict = model.get_all_data_by_dict()
        )

        return UserData.create_object(**converted_dict)

