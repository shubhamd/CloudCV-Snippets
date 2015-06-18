from twisted.internet.defer import Deferred
import time
def fun(name):
	print "hello ",name
	time.sleep(2)
	print "I am awake"
	return "shoooo"

def fun1(arg):
	print "this is my misterious arg",arg
	print "I am here because the first one is sleeping"

d = Deferred()
d.addCallback(fun)
d.addCallback(fun1)
d.callback("shubham")