import threading 
from Queue import Queue 


class UploadThread(Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception, e: 
                print e
            self.tasks.task_done()

class UploadPool:
    
    def __init__(self, num_of_threads):
        
        self.udtasks = Queue(num_of_threads)
        
        for _ in range(num_threads):
            UploadThread(self.udtasks) 

    def add_to_upload(self, UploadObj, *args, **kargs):
        self.udtasks.put((UploadObj, args, kargs))

    def wait_untill_completion(self):
        self.udtasks.join()