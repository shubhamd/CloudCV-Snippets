from __future__ import print_function
import sys
from os import listdir
images = listdir("/home/shubham/Pictures/source")

import gevent
from gevent import monkey

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()



from urllib2 import urlopen


def print_head(url):    
    data = urlopen(url).read()
    

jobs = [gevent.spawn(print_head, "http://localhost:8000/"+url) for url in images]

gevent.wait(jobs)