from re import compile, IGNORECASE
from base64 import b64encode
from string import ascii_lowercase
from random import randint, choice
import hashlib

url_validator = compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', IGNORECASE)

def join_abs_paths(paths,sep = '/'):
    return sep.join([p.strip(sep) for p in paths])


def b64_chunks(l, n):
    return [b64encode(l[i:i+n]) for i in range(0, len(l), n)]

def randstr(n = 4, fixed = True, charset = None):
    if not fixed:
        n = randint(1,n)
    
    if not charset:
        charset = ascii_lowercase
        
    return ''.join(choice(charset) for x in range(n))
 
def md5sum(filename):
   md5 = hashlib.md5()
   with open(filename,'rb') as f: 
       for chunk in iter(lambda: f.read(128*md5.block_size), b''): 
            md5.update(chunk)
   return md5.hexdigest()   