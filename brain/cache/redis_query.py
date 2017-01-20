#!/usr/bin/python

'''

This file allows various redis data structures to be used for caching.

'''

import redis
from brain.cache.redis_settings import Redis_Settings


class Redis_Query(object):
    '''

    This class provides an interface to various Redis data structures.
    Specifically, caching, and uncaching methods are provided for the
    following redis data structures:

        - strings
        - lists
        - sets
        - hashes

    Note: this class requires the implementation of the 'start_redis' method,
          in order to execute the below redis methods.

    Note: for persistence, it may be a good idea to create an instance of
          this class in the global scope.

    Note: 'sorted sets' methods were not included, since it is similar in
          concept to 'lists'. Also, the above included redis data structures,
          provides enough flexibility to accomplish most requirements.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, db_num=0, host=None, port=None):
        '''

        This constructor defines necessary redis attributes, used to define a
        connection between the client, and redis server.

        @db, the redis database number to store jobs into (there are 0-15).

        Note: we implement the 'StrictRedis' class, which adheres to the strict
              redis syntax, not the backwards compatibile subclass, 'Redis'.

        Note: this class explicitly inherits the 'new-style' class.

        '''

        # redis settings
        my_redis = Redis_Settings()

        # define host, and port, if provided
        if host:
            my_redis.set_host(host)
        if port:
            my_redis.set_port(port)

        # get redis parameters
        self.host = my_redis.get_host()
        self.port = my_redis.get_port()
        self.db_num = db_num

    def start_redis(self):
        '''

        This method establishes a redis instance.

        @pool, we define a reusable connection pool, based on the supplied
            host, port, and db_num. This allows the redis client (StrictRedis)
            to reuse a previous connection within the pool, which may be idle
            from previous use.

        Note: a connection pool manages a set of connection instances. By
              default, the maximum limit is 10,000 concurrent connections, and
              can be adjusted within 'redis.conf' (maxmemory directive).

        Note: for more information regarding redis concurrent client
              connections, review the following:

              https://github.com/jeff1evesque/machine-learning/issues/1761

        '''

        pool = redis.ConnectionPool(
            host=self.host,
            port=self.port,
            db=self.db_num
        )
        self.server = redis.StrictRedis(connection_pool=pool)

    def shutdown(self):
        '''

        This method shuts down an established redis instance.

        '''

        if self.server and type(self.server) == redis.client.StrictRedis:
            self.server.shutdown()

    def bgsave(self):
        '''

        This saves the current redis data to disk, in the background
        (asynchronously).

        Note: the corresponding dump file can be found in the 'redis.conf'
              file, associated with 'dbfilename'. By default, it is called
              'dump.rdb'.

        '''

        self.server.bgsave()

    def set(self, key, value):
        '''

        This method caches the provided key-value into a redis set data
        structure.

        Note: by default, redis keys are created without an associated time to
              live.  Therefore, the key will live until it is explicitly
              removed.

        '''

        self.server.set(key, value)

    def setex(self, key, value, time):
        '''

        This method is responsible for setting the provided key-value into a
        redis set data structure, with an expire time (in seconds).

        '''

        self.server.set(key, value, time)

    def expire(self, key, time):
        '''

        This sets an expire time (in seconds), for an existing redis object.

        '''

        self.server.expire(key, time)

    def persist(self, name):
        '''

        This removes an expire time (in seconds), for an existing redis object.

        '''

        self.server.persist(name)

    def rename(self, src, dst):
        '''

        This method renames an existing redis object.

        '''

        self.server.rename(src, dst)

    def type(self, name):
        '''

        This method returns the type of the provided redis object.

        '''

        return self.server.type(name)

    def get(self, key):
        '''

        This method returns the redis value, using the provided key.

        '''

        return self.server.get(key)

    def delete(self, key):
        '''

        This method deletes the desired redis structure, using the provided
        key.

        '''

        self.server.delete(key)

    def lset(self, name, index, value):
        '''

        This method assigns an index for the provided value, within the
        respective list.

        '''

        self.server.lset(name, index, value)

    def lindex(self, name, index):
        '''

        This method returns the element at index in the list stored at key.

        '''

        return self.server.lindex(name, index)

    def lrem(self, name, count, value):
        '''

        This method removes the first count occurrences of elements equal to
        value within the redist list.

        '''

        self.server.lrem(name, count, value)

    def lpush(self, name, *values):
        '''

        This method pushes the provided values onto the beginning of a redis
        list.

        '''

        self.server.lpush(name, *values)

    def rpush(self, name, *values):
        '''

        This method pushes the provided values onto the ending of a redis
        list.

        '''

        self.server.rpush(name, *values)

    def lpop(self, name):
        '''

        This method removes, and returns the first item of the specified redis
        list.

        '''

        return self.server.lpop(name)

    def rpop(self, name):
        '''

        This method removes, and returns the last item of the specified redis
        list

        '''

        return self.server.rpop(name)

    def ltrim(self, name, start, end):
        '''

        This method trims the redis list, removing all elements not within the
        slice bounds.

        '''

        self.server.ltrim(name, start, end)

    def lrange(self, name, start, end):
        '''

        This method returns a slice of the redis list between the slice
        bounds.

        '''

        return self.server.lrange(name, start, end)

    def llen(self, name):
        '''

        This method returns the length of the redis list.

        '''

        return self.server.llen(name)

    def hdel(self, name, *keys):
        '''

        This method deletes a value from the redis hash.

        '''

        self.server.hdel(name, *keys)

    def hexists(self, name, key):
        '''

        This method returns a boolean if a key exists within the specified
        redis hash.

        '''

        return self.server.hexists(name, key)

    def hget(self, name, key):
        '''

        This method returns a value from the specified redis hash.

        '''

        return self.server.hget(name, key)

    def hset(self, name, key, value):
        '''

        This method sets a value into a redis hash.

        '''

        self.server.hset(name, key, value)

    def hvals(self, name):
        '''

        This method returns the list of values within the specified redis
        hash.

        '''

        return self.server.hvals(name)

    def hlen(self, name):
        '''

        This method returns the number of elements within the specified redis
        hash.

        '''

        return self.server.hlen(name)

    def hkeys(self, name):
        '''

        This method returns the list of keys within the specified redis hash.

        '''

        return self.server.hkeys(name)

    def sadd(self, name, *values):
        '''

        This method adds values to the specified redis set.

        '''

        self.server.sadd(name, *values)

    def scard(self, name):
        '''

        This method returns the number of elements with the specified redis
        set.

        '''
        return self.server.scard(name)

    def sinter(self, keys, *args):
        '''

        This method returns the intersection between redis sets, specified
        by the multiple supplied keys.

        '''

        return self.server.sinter(keys, *args)

    def sismember(self, name, value):
        '''

        This method returns a boolean if the specified value exists within the
        specified redis set.

        '''

        return self.server.sismember(name, value)

    def smembers(self, name):
        '''

        This method returns all members of the specified redis set.

        '''

        return self.server.smembers(name)

    def srem(self, name, *values):
        '''

        This method removes values from the specified redis set.

        '''

        return self.server.srem(name, *values)

    def sunion(self, keys, *args):
        '''

        This method returns the union between redis sets, specified
        by the multiple supplied keys.

        '''

        return self.server.sunion(keys, *args)

    def sunionstore(self, key, *args):
        '''

        This method stores the union between redis sets, specified
        by the multiple supplied keys (*args), into a redis set
        designated by 'key'.

        '''

        return self.server.sunionstore(key, *args)
