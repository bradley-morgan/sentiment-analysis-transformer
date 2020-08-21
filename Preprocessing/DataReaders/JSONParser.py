import gzip
import json
import sys


def JSONParser(path, batch_size):
    g = gzip.open(path, 'r')
    for l in g:
        k = json.loads(l)
        yield k

