import redis


class RedisDB(object):

    def add_data(self, key, name, position):
        redis_request = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        redis_request.hmset(key, {'name': name, 'position': position})

    def extract_name_by_key(self, data_key):
        redis_request = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        name_by_key = str(redis_request.hget(data_key, 'name')).split('\'')[1]
        return name_by_key

    def extract_position_by_key(self, data_key):
        redis_request = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        position_by_key = str(redis_request.hget(data_key, 'position')).split('\'')[1]
        return position_by_key

    def delete_data_by_key(self, data_key):
        redis_request = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        return redis_request.delete(data_key)

    def clear_all_data(self):
        redis_request = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        return redis_request.flushall()



