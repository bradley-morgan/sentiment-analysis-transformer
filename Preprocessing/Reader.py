import gzip
import json

def JSONparser(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield json.loads(l)



data_src = '../Datasets/Books_5.json.gz'

data_gen = JSONparser(data_src)

for i, data in enumerate(data_gen):
  print(data)




