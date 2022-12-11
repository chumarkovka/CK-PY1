# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

def dict(p):
    return{'bin': bin(p), 'dec': p, 'hex': hex(p), 'oct': oct(p)}

pprint([dict(l) for l in range(16)])
