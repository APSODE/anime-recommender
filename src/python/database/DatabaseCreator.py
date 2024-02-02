import os.path

from typing import Optional
from urllib.parse import quote_plus
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database


from src.python.utils.JsonReadWrite import JsonReadWrite


class _DatabaseAccount:
    def __init__(self):
        self.CURRENT_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
        self._account_data_file = os.path.join(self.CURRENT_FILE_PATH, "database_account.json")
        self._id = ""
        self._pw = ""
        self._read_data()

    def _read_data(self) -> None:
        ac_data = JsonReadWrite.ReadJson(
            self._account_data_file
        )
        self._id = quote_plus(ac_data.get("id"))
        self._pw = quote_plus(ac_data.get("pw"))

    @property
    def id(self):
        return self._id

    @property
    def pw(self):
        return self._pw


class DatabaseCreator:
    Model: DeclarativeMeta = declarative_base()
    _single_instance = None

    def __new__(cls):
        if cls._single_instance is None:
            cls._single_instance = super(DatabaseCreator, cls).__new__(cls)

        return cls._single_instance

    def __init__(self):
        cls = type(self)

        if not hasattr(cls, "__init"):
            self._database_account = _DatabaseAccount()
            self._engine = self._create_engine()
            self._session = self._create_session()
            self.Model.query = self._session.query_property()
            self.init_db()

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine

    @staticmethod
    def create_object() -> "DatabaseCreator":
        return DatabaseCreator()

    def _create_engine(self) -> Engine:
        # create_database(f"mysql+pymysql://{self._database_account.id}:{self._database_account.pw}@127.0.0.1:3306/arws_db")
        return create_engine(
            f"mysql+pymysql://{self._database_account.id}:{self._database_account.pw}@127.0.0.1:3306/arws_db",
            echo = True
        )

    def _create_session(self) -> scoped_session:
        return scoped_session(
            session_factory = sessionmaker(
                autoflush = False,
                bind = self._engine,
                autocommit = False
            )
        )

    def init_db(self) -> None:
        self.Model.metadata.create_all(bind = self._engine)


