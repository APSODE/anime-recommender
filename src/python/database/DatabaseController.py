import inspect
import traceback

from sqlalchemy.sql.elements import BinaryExpression
from sqlalchemy.orm.query import Query
from typing import Iterable, Optional, List, TypeVar, Union, Type
from src.python.database.DatabaseCreator import DatabaseCreator
from src.python.custom_typing.ModelTypes import ModelType


T = TypeVar("T")


class DatabaseController:
    _single_instance = None

    def __new__(cls):
        if cls._single_instance is None:
            cls._single_instance = super(DatabaseController, cls).__new__(cls)

        return cls._single_instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "__init"):
            self.count = 0
            self._database_creator = DatabaseCreator.create_object()

    @property
    def db_creator(self) -> DatabaseCreator:
        return self._database_creator

    @staticmethod
    def create_object() -> "DatabaseController":
        return DatabaseController()

    def _get_filtered_data(self,
                           model_class: Union[ModelType, Type[ModelType]],
                           filter: BinaryExpression[bool] | None = None) -> Query:

        filtered_data = self._database_creator.session.query(
            model_class
        )

        if filter is not None:
            return filtered_data.filter(
                filter
            )

        return filtered_data

    def add_data(self, model: Union[ModelType, Iterable[ModelType]], with_commit: bool = False):
        if isinstance(model, Iterable):
            self._database_creator.session.add_all(model)

        else:
            self._database_creator.session.add(model)

        if with_commit:
            self.commit_data()

    def get_data(self,
                 model_class: T,
                 filter: BinaryExpression[bool] | None = None,
                 amount: int = 0) -> Optional[Union[List[T], T]]:
        """
        :param model_class: 모델 구현 클래스 (BaseModel 클래스를 상속 받은 클래스를 사용)
        :param filter: <Type[BaseModel]>.<column_name> == filter_data
        :param amount: 필터링을 통해 가져올 데이터 개수 (default: 0 -> 0일 경우 모든 데이터를 가져옴)
        :return:
        """
        filtered_data = self._get_filtered_data(
            model_class = model_class,
            filter = filter
        )

        if amount == 0:
            return filtered_data.all()

        elif amount == 1:
            return filtered_data.limit(amount).first()

        else:
            return filtered_data.limit(amount).all()

    def edit_data(self,
                  model_class: Union[ModelType, Type[ModelType]],
                  update_data: dict,
                  filter: BinaryExpression[bool] | None = None,
                  with_commit: bool = False):

        filtered_data = self._get_filtered_data(
            model_class = model_class,
            filter = filter
        )

        filtered_data.update(update_data)

        if with_commit:
            self.commit_data()

    def delete_data(self,
                    model_class: Union[ModelType, Type[ModelType]],
                    filter: BinaryExpression[bool] | None = None,
                    amount: int = 1):

        filtered_data = self._get_filtered_data(
            model_class = model_class,
            filter = filter
        )

        if amount == 1:
            selected_data = filtered_data.first()

        else:
            selected_data = filtered_data.limit(amount)

        self._database_creator.session.delete(selected_data)

    def rollback(self):
        self._database_creator.session.rollback()

    def commit_data(self):
        # self.count += 1
        # print(f"{self.count}번째 커밋 메소드 호출")
        # print(inspect.getframeinfo(inspect.currentframe().f_back))
        # print(traceback.extract_stack()[-2])
        self._database_creator.session.commit()

    def is_already_exist(self,
                         model_class: Union[ModelType, Type[ModelType]],
                         filter: BinaryExpression[bool] | None) -> bool:

        filtered_data = self._get_filtered_data(
            model_class = model_class,
            filter = filter
        )

        return len(filtered_data.all()) >= 1

    def drop_all_table(self):
        self._database_creator.Model.metadata.drop_all(bind = self._database_creator.engine)
        self._database_creator.init_db()

