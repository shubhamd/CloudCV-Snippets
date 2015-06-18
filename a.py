import multiprocessing 

class PCloudCV(multiprocessing.Process):
	def __init__(self):
		multiprocessing.Process.__init__(self)
		print "new obj created"

	def run(self):
		print "started running in a new thread"
		

	def classify(self):
		print "start1 called"
		self.start()
		self.join()

	def imageStitch(self):
		print "start2 called"
		self.start()
		self.join()

pcv = PCloudCV()
pcv.classify()
pcv.imageStitch()
