
from twisted.internet import reactor,defer 

url = 'http://google.com'


def getPage():
	t = 10**8
	d = defer.Deferred()
	d.addCallback(loopFunction)
	return d 

def loopFunction():
	print "now looping"
	t = 10
	while t :
		t-=1
	print "loop finished"

def print_and_stop(output):
    print output
    if reactor.running:
       reactor.stop()

print 'fetching', url
d = getPage()
print "this is some code not related to the code"
d.addCallback(print_and_stop)
reactor.run()