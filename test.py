#!/usr/bin/python
import redis
for i in range (16):

    r = redis.Redis(host='119.28.41.227',port=32320,db=i)
    with r.pipeline(transaction=False) as p:
            for key in range(2,1000000000):
               p.sadd(key, key+1)
            p.execute()
