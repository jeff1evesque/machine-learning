#!/usr/bin/python

## @redis_query.py
#  This file contains the required class to set, get, and delete various
#      redis-cached objects.
import redis
from brain.cache.redis_settings import Redis_Settings

## Class: Redis_Query, explicitly inherit 'new-style' class.
#
#  Note: we have included methods for the following redis data structures:
#
#      - strings
#      - lists
#      - sets
#      - hashes
#
#  Note: 'sorted sets' methods were not included, since it is similar in
#        concept to 'lists'. Also, the above included redis data structures,
#        provides enough flexibility to accomplish most requirements.
class Redis_Query(object):

    ## constructor: defines class variables.
    #
    #  @db, the redis database number to store jobs into (there are 0-15).
    #
    #  Note: we implement the 'StrictRedis' class, not its subclass 'Redis',
    #        which provides backwards compatibility with older versions of redis.
    def __init__(self, db_num=0, host=None, port=None):
        # get redis settings
        my_redis = Redis_Settings()

        # define host, and port, if provided
        if host:
            my_redis.set_host(host)
        if port:
            my_redius.set_port(port)

        # invoke 'StrictRedis', not the older backwards compatible 'Redis'
        self.host   = my_redis.get_host()
        self.port   = my_redis.get_port()
        self.db_num = db_num
        self.server = redis.StrictRedis(host=self.host, port=self.port, db=db_num)

    ## set: set value into redis server.
    #
    #  Note: by default, redis keys are created without an associated time
    #        to live.  Therefore, the key will live until it is explicityl
    #        removed.
    def set(self, key, value):
        self.server.set(key, value)
 
    ## setex: set value into redis server, with an expire time (in seconds).
    def setex(self, key, value, time):
        self.server.set(key, value, time)

    ## expire: set an expire time (in seconds) for existing redis object.
    def expire(self, key, time):
        self.server.expire(key, time)

    ## persist: removes an expire time for an existing redis object.
    def persist(self, name):
      self.server.persist(name)

    ## rename: renames a redis object.
    def rename(self, src, dst):
        self.server.rename(src, dst)

    ## type: return the type of a redis object.
    def type(self, name):
        return self.server.type(name)

    ## get: retrieve value from redis server.
    def get(self, key):
        return self.server.get(key)
 
    ## delete: delete value from redis server.
    def delete(self, key):
        self.server.delete(key)

    ## lset: set value to the index of the redis list.
    def lset(self, name, index, value):
        self.server.lset(name, index, value)

    ## lindex: return the element as defined redis list index.
    def lindex(self, name, index):
        return self.server.lindex(name, index)

    ## lrem: remove the first count occurences of elements equal to value
    #        within the redist list.
    def lrem(self, name, count, value)
        self.server.lrem(name, count, value)

    ## lpush: push values onto the beginning of a redis list.
    def lpush(self, name, *values):
        self.server.lpush(name, *values)

    ## rpush: push values onto the ending of a redis list.
    def rpush(self, name, *values):
        self.server.rpush(name, *values)

    ## lpop: remove, and return the first item of the redis list.
    def lpop(self, name):
        return self.server.lpop(name)

    ## rpop: remove, and return the last item of the redis list.
    def rpop(self, name):
        return self.server.rpop(name)

    ## ltrim: trim the redis list, removing all elements not within the
    #         slice bounds.
    def ltrim(self, name, start, end):
        self.server.ltrim(name, start, end)

    ## lrange: return a slice of the redis list between the slice bounds.
    def lrange(self, name, start, end):
        return self.server.lrange(name, start, end)

    ## llen: return the length of the redis list.
    def llen(self, name):
        return self.server.llen(name)

    ## hdel: delete value from redis hash.
    def hdel(self, name, *keys):
        self.server.hdel(name, *keys)

    ## hexists: returns a boolean of a key exists within a redis hash.
    def hexists(self, name, key):
        return self.server.hexists(name, key)

    ## hget: returns a value from a redis hash.
    def hget(self, name, key):
        return self.server.hget(name, key)

    ## hset: set value into a redis hash.
    def hset(self, name, key, value):
        return self.server.hset(name, key, value)

    ## hvals: return the list of values within the redis hash.
    def hvals(self, name):
        return self.server.hvals(name)

    ## hlen: return the number of elements within the redis hash.
    def hlen(self, name):
        return self.server.hlen(name):

    ## hkeys: return the list of keys within the redis hash
    def hkeys(self, name):
        return self.server.hkeys(name)

    ## sadd: add values to redis set.
    def sadd(self, name, *values):
        self.server.sadd(name, *values)

    ## scard: return the number of elements in a redis set.
    def scard(self, name):
        return self.server.scard(name)

    ## sinter: return the intersection of redis sets.
    def sinter(self, keys, *args):
        return self.server.sinter(keys, *args)

    ## sismember: returns a boolean if define value is in redis set.
    def sismember(self, name, value):
        return self.server.sismember(name, value)

    ## smembers: return all members in a redis set.
    def smembers(self, name):
        return self.server.smembers(name)

    ## srem: remove values from redis set.
    def srem(self, name, *values):
        return self.server.srem(name, *values)

    ## sunion: return the union of redis sets.
    def sunion(self, keys, *args):
        return self.server.sunion(keys, *args)

    ## sunionstore: store the union of redis sets into a new redis set.
    def sunionstore(self, keys, *args):
        return self.server.sunionstore(keys, *args)
