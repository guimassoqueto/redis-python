import redis
from json import dumps, loads
from sys import argv
from os.path import exists
from os import remove


def get_pids_list_from_file(file_name: str):
  pids = []
  if exists(file_name):
      with open(file_name, 'r', encoding='utf-8') as f:
          for line in f:
              line = line.strip()
              if line: pids.append(line)
      if pids: return pids
      raise NameError(f'{file_name} file is empty')
  else:
      raise FileNotFoundError(f'{file_name} file not found')


if __name__ == "__main__":
  try:
    pids_file = input('Insert pids file name: ')
    pids_list = get_pids_list_from_file(pids_file)

    r = redis.Redis(host='localhost', port=6379, db=0)
    if r.get('amazon_pids'): r.delete('amazon_pids')
    r.set('amazon_pids', dumps(pids_list))
  except Exception as e:
    print(str(e))


# r = redis.Redis(host='localhost', port=6379, db=0)

# if r.get('amazon_pids'): r.delete('amazon_pids')
# l= []
# r.set('amazon_pids', dumps(l))

