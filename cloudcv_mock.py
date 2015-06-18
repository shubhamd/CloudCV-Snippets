from twisted.internet import defer, reactor 


class CloudCV():

	def __init__(self):
	# some stuff 
		self.d = defer.Deferred()
		pass 

	def classify(self, exec="classify"):
		
		reactor.callLater(1, self.UploadData, path)
		
		self.d.addCallback(1, self.socketIO)
		reactor.run()

	def features(self, exec="features"):
		reactor.callLater(1, self.UploadData, path)
		reactor.callLater(1, self.socketIO, path)
		print exec
		reactor.run()	

	def addConfig():
		# adds config params from the config.json or command line args 
		print "config added"

	def uploadData(path): # location : UploadData.sendPostRequest 
	# convert current calls to async data uploading APIs from twsited 
		print "Uploading data..."

		if (config.exec=="features")
			self.d.addCallback(self.features)
		
		if (config.exec=="classify")
			self.d.addCallback(self.classify)
		self.d.callback(flag)
	
	def printData(result):
		print result
		reactor.stop()
	
	def printError(failure):
		print failure
		reactor.stop()

pcv = CloudCV() 

pcv.classify() 
pcv.features()


