#coding=utf8
#__author__ = 'wanghf'
import tornado.web

class CacheHandler(tornado.web.RequestHandler):
    cache ={}
    cache_size = 200

    @classmethod
    def save(cls, key,value):
      cls.cache.setdefault(key,value)
      if len(cls.cache) > cls.cache_size:
         cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def list(cls):
        return cls.cache

    @classmethod
    def get(cls,id):
        return cls.cache.get(id)

    @classmethod
    def clear(cls,id):
        return cls.cache.pop(id)