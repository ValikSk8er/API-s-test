import json

from data.redis_db import RedisDB
from config import use_redis
from data.test_data import candidate_data
from pages.candidates import Candidate

class DataDriven(object):

    to_use_redis = use_redis
    db = RedisDB()
    can = Candidate()

    def generate(self):
        if self.to_use_redis:
            for candidate in candidate_data:
                key = candidate[0]
                name = candidate[1]
                position = candidate[2]
                self.db.add_data(key, name, position)

    def get_name(self, key):
        if self.to_use_redis:
            return self.db.extract_name_by_key(key)
        else:
            for cand in candidate_data:
                if cand[0] == key:
                    return cand[1]

    def get_position(self, key):
        if self.to_use_redis:
            return self.db.extract_position_by_key(key)
        else:
            for cand in candidate_data:
                if cand[0] == key:
                    return cand[2]

    @property
    def get_list_data(self):
        return json.loads(self.can.get_list.content)["candidates"]

if __name__ == "__main__":
    DataDriven()
