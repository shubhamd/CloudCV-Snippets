import gevent
from gevent import greenlet

class MyGreenlet(greenlet):

    def __init__(self, message, n):
        greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)

g = MyGreenlet("Hi there!", 3)
g.start()
g.join()