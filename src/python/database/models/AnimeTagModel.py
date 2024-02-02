from typing import TYPE_CHECKING, Dict, Any

from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from src.python.database.DatabaseCreator import DatabaseCreator
from src.python.database.models.BaseModel import BaseModel


_BACK_POPULATES_PARAMS = "anime_tag_model"


class AnimeTagModel(BaseModel, DatabaseCreator.Model):
    __tablename__ = "anime_tag"
    __table_args__ = (
        PrimaryKeyConstraint(
            "anime_id",
            "tag_id",
            name = "anime_tag_constraint"
        ),
    )

    anime_id = Column(Integer, ForeignKey("anime.id"), nullable = False)
    tag_id = Column(Integer, ForeignKey("tag.id"), nullable = False)

    # from src.python.database.models.AnimeModel import AnimeModel
    anime_model = relationship(
        "AnimeModel",
        back_populates = _BACK_POPULATES_PARAMS
    )

    tag_model = relationship(
        "TagModel",
        back_populates = _BACK_POPULATES_PARAMS
    )

    def __init__(self, anime_id: int, tag_id: int):
        self.anime_id = anime_id
        self.tag_id = tag_id
        super().__init__()

    def get_all_data_by_dict(self) -> Dict[str, Any]:
        return super().get_all_data_by_dict()

    @staticmethod
    def create_model(anime_id: int, tag_id: int) -> "AnimeTagModel":
        return AnimeTagModel(
            anime_id = anime_id,
            tag_id = tag_id
        )

    @staticmethod
    def convert_to_dto(model):
        pass