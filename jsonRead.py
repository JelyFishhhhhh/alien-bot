import orjson
from orjson import loads
from copy import deepcopy

class json:
    def load(file: str) -> dict | list:

        with open(file, mode='r', encoding='utf8') as in_file:
            res = orjson.loads(in_file.read())

        return deepcopy(res)