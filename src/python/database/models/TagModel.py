from typing import Dict, Any, TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.python.database.DatabaseCreator import DatabaseCreator
from src.python.database.models.BaseModel import BaseModel


_BACK_POPULATES_PARAMS = "tag_model"


class TagModel(BaseModel, DatabaseCreator.Model):
    __tablename__ = "tag"

    id = Column(Integer, primary_key = True)
    name = Column(String(32), nullable = False)

    # relationship 정의 과정에서 순환참조 문제가 발생하는 것을 해결하기 위해
    # 모델 클래스를 문자열을 사용해 지정하는 것이 아닌 직접 클래스를 이용해 지정하였음
    from src.python.database.models.AnimeTagModel import AnimeTagModel
    anime_tag_model = relationship(
        AnimeTagModel,
        back_populates = _BACK_POPULATES_PARAMS
    )

    # relationship 정의 과정에서 순환참조 문제가 발생하는 것을 해결하기 위해
    # 모델 클래스를 문자열을 사용해 지정하는 것이 아닌 직접 클래스를 이용해 지정하였음
    from src.python.database.models.TagWeightModel import TagWeightModel
    tag_weight_model = relationship(
        TagWeightModel,
        back_populates = _BACK_POPULATES_PARAMS
    )

    def __init__(self, name: str):
        self.name = name
        super().__init__()

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return super().get_all_data_by_dict()

    @staticmethod
    def create_model(name: str) -> "TagModel":
        return TagModel(name = name)

    @staticmethod
    def convert_to_dto(model):
        pass


