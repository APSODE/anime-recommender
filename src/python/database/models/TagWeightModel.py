from typing import TYPE_CHECKING, Dict, Any

from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from src.python.database.DatabaseCreator import DatabaseCreator
from src.python.database.models.BaseModel import BaseModel


_BACK_POPULATES_PARAMS = "tag_weight_model"


class TagWeightModel(BaseModel, DatabaseCreator.Model):
    __tablename__ = "tag_weight"
    __table_args__ = (
        PrimaryKeyConstraint(
            "user_id", "tag_id",
            name = "user_tag_constraint"
        ),
    )

    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    tag_id = Column(Integer, ForeignKey("tag.id"), nullable = False)
    weight = Column(Integer, default = 0, nullable = False)

    user_model = relationship(
        "UserModel",
        back_populates = _BACK_POPULATES_PARAMS
    )

    tag_model = relationship(
        "TagModel",
        back_populates = _BACK_POPULATES_PARAMS
    )

    def __init__(self, user_id: int, tag_id: int, weight: int):
        self.user_id = user_id
        self.tag_id = tag_id
        self.weight = weight

        super().__init__()

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return super().get_all_data_by_dict()

    @staticmethod
    def create_model(user_id: int, tag_id: int, weight: int) -> "TagWeightModel":
        return TagWeightModel(
            user_id = user_id,
            tag_id = tag_id,
            weight = weight
        )

    @staticmethod
    def convert_to_dto(model):
        pass