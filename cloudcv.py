import os
import threading
from connections import local_server
from utility import accounts, logging
from utility.parseArguments import ConfigParser
from connections.uploadData import UploadData
from connections.socketConnection import SocketIOConnection

from threadpool import UploadPool

class PCloudCV(threading.Thread):
    
    config_obj = None

    def __init__(self, file, list, login_required=True):
        threading.Thread.__init__(self)
        
        
        self._num_threads = 5 
        self.pool = UploadPool(5)


        self.login_required = login_required
        accounts.login_required = login_required

        self.config_obj = ConfigParser()
        self.config_obj.parseArguments(list, file)
        self.config_obj.verify()

        local_server.server.setDaemon(True)
        local_server.server.start()

        self.ud = UploadData(self.config_obj)
        self.sioc = SocketIOConnection(self.config_obj.exec_name, self.config_obj.output_path)
        self.sioc.setDaemon(True)
        self.ud.setDaemon(True)

    def stop_local_server(self):
        
        local_server.server.stop()

    def signal_handler(self, signal, frame):
        
        print '\nYou pressed Ctrl+C! Exiting Now'
        local_server.server.stop()
        local_server.exit_program()

    def dropbox_authenticate(self):

        accounts.dropboxAuthenticate()

    def authenticate(self):
        
        
    def run(self):
        if self.login_required:
            accounts.authenticate()

        self.sioc.start()
        
