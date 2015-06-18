import requests 
from time import time 
from os import listdir

images = listdir("/home/shubham/Pictures/source")

then = time()
images = images[:50]
print(len(images))
for i in images:	
	response = requests.get("http://localhost:8888/"+i)
print("Total time taken",time()-then)