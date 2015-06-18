from twisted.internet import reactor, defer
import time
from threading import Thread



class CloudCV(): 
    def someCallback(self, result, previous_data):
        # here we pass the result of the deferred down the callback chain
        # (done synchronously)
        d = defer.Deferred()
        print "calling function 1 on result:%s with previous result:%s %s" % (result, previous_data,time.time())
        return d

    # To be imported from the connections package
    def uploadData(self, executable_name):
        # so we can do asynchronous stuff here, 
        # like firing something 1 second later and have 
        # another method processing the result

        print "Uploading Data for :%s %s" % (executable_name,time.time())
         
        d = defer.Deferred()
        reactor.callLater(1, d.callback, "second callback")
        d.addCallback(self.someCallback, executable_name)
        return d 

    # TODO : Add startReactor as a decorator 
    def startReactor(self):
        if not reactor.running:
            Thread(target=reactor.run, args=(False,)).start()
    
    def classify(self):
        
        print "Entered classify"
        d = defer.Deferred()
        reactor.callLater(1, d.callback, "classify")
        d.addCallback(self.uploadData)
        self.startReactor()
        return d 

    def imageStitch(self):
        print "Entered imageStitch"
        
        d = defer.Deferred()
        reactor.callLater(1, d.callback, "imageStitch")
        d.addCallback(self.uploadData)
        print "Reactor status from function is ", reactor.running
        self.startReactor()
        return d 

pcv = CloudCV()
print "Start : some random code by programmer"
pcv.classify()
print "Start : some random code by programmer"
pcv.imageStitch()
print "Reactor status is", reactor.running

