import redis
from json import dumps, loads

r = redis.Redis(host='localhost', port=6379, db=0)

some_list = ["lula", "bolsonaro"]

r.set('amazon_pids', dumps(some_list)) # dumps: convert array to string 

# pids = loads(r.get('amazon_pids'))
# print(pids)
#r.delete('amazon_pids')

