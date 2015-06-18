from twisted.web.client import getPage
from os import listdir
from twisted.internet import defer,task, reactor
from time import time
images = listdir("/home/shubham/Pictures/source")
# images = images[:50]
url = "http://localhost:8888/"

@defer.inlineCallbacks
def get_multiple(pages):
  results = yield defer.DeferredList([getPage(url) for url in pages])
  defer.returnValue(results)

  
t = task.deferLater(reactor, 0, get_multiple, [url+i for i in images])
t.addBoth(lambda _: reactor.stop())
reactor.run()