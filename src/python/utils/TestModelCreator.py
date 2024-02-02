from typing import Optional

from src.python.database.DatabaseController import DatabaseController
from src.python.database.models.AnimeModel import AnimeModel
from src.python.database.models.AnimeTagModel import AnimeTagModel
from src.python.database.models.TagModel import TagModel
from src.python.database.models.TagWeightModel import TagWeightModel
from src.python.database.models.UserModel import UserModel


__all__ = ["TestModelCreator"]


class TestModelCreator:
    @staticmethod
    def create_test_anime_model() -> AnimeModel:
        return AnimeModel(title = "test_anime_title", description = "test_anime_description")

    @staticmethod
    def create_test_tag_model() -> TagModel:
        return TagModel.create_model(name = "test_tag")

    @staticmethod
    def create_test_user_model() -> UserModel:
        return UserModel.create_model(account_id = "test_user_id", account_pw = "test_user_pw")

    @staticmethod
    def create_test_tag_weight_model() -> TagWeightModel:
        db_controller = DatabaseController.create_object()
        db_user = db_controller.get_data(
            model_class = UserModel,
            filter = UserModel.account_id == "test_user_id",
            amount = 1
        )
        db_tag = db_controller.get_data(
            model_class = TagModel,
            filter = TagModel.name == "test_tag",
            amount = 1
        )

        return TagWeightModel(
            user_id = db_user.id,
            tag_id = db_tag.id,
            weight = 100
        )

    @staticmethod
    def create_test_anime_tag_model() -> AnimeTagModel:
        db_controller = DatabaseController.create_object()
        db_anime = db_controller.get_data(
            model_class = AnimeModel,
            filter = AnimeModel.title == "test_anime_title",
            amount = 1
        )
        db_tag = db_controller.get_data(
            model_class = TagModel,
            filter = TagModel.name == "test_tag",
            amount = 1
        )

        return AnimeTagModel(
            anime_id = db_anime.id,
            tag_id = db_tag.id
        )
