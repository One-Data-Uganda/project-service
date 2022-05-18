import redis

from app.core.config import settings


class RedisOperation(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            pool = redis.ConnectionPool(
                host=settings.REDIS_HOST, port=settings.REDIS_PORT
            )
            cls.instance = redis.StrictRedis(connection_pool=pool)
        return cls.instance


cache = RedisOperation()
