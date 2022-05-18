from typing import Optional

from aioredis import Redis, create_redis_pool

from app.core.config import settings


class RedisCache:
    def __init__(self):
        self.redis_cache: Optional[Redis] = None

    async def init_cache(self):
        self.redis_cache = await create_redis_pool(settings.REDIS_URL)

    async def keys(self, pattern):
        if not self.redis_cache:
            return None
        return await self.redis_cache.keys(pattern)

    async def set(self, key, value):
        if not self.redis_cache:
            return None
        return await self.redis_cache.set(key, value)

    async def get(self, key):
        if not self.redis_cache:
            return None
        return await self.redis_cache.get(key)

    async def hget(self, key, val):
        if not self.redis_cache:
            return None
        return await self.redis_cache.hget(key, val)

    async def hgetall(self, key):
        if not self.redis_cache:
            return None
        return await self.redis_cache.hgetall(key)

    async def hset(self, key, idx, val):
        if not self.redis_cache:
            return None
        return await self.redis_cache.hset(key, idx, val)

    async def hdel(self, key, idx):
        if not self.redis_cache:
            return None
        return await self.redis_cache.hdel(key, idx)

    async def close(self):
        self.redis_cache.close()
        await self.redis_cache.wait_closed()


cache = RedisCache()
