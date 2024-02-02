from typing import Union, Type, Iterable
from src.python.database.models.BaseModel import BaseModel

_MODELS_COMMON_TYPE = Union[BaseModel, Type[BaseModel]]  # BaseModel을 상속 받거나 BaseModel의 구현체만

ModelType = Union[_MODELS_COMMON_TYPE, Iterable[_MODELS_COMMON_TYPE]]