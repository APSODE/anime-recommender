from typing import Optional
from src.python.database.DatabaseController import DatabaseController


# 싱글톤을 적용시켜야할까? 고민해보고 나중에 싱글톤 패턴 적용여부 결정할 것
class Finder:
    def __init__(self, db_controller: DatabaseController):
        self._db_controller = db_controller

    def search(self, keyword: str):
        # 단순히 순회를 도는 방식의 검색 방식이면
        # O(N)의 시간 복잡도
        # 최적화 방식을 고민할 것.
        pass






