import aiohttp 
import asyncio 
from time import time
from os import listdir 

images = listdir("/home/shubham/Pictures/source")

images = images[:50]
print(len(images))
@asyncio.coroutine 
def get_image(url):
	for i in images:
	    response = yield from aiohttp.request('GET', url+i)

loop = asyncio.get_event_loop()
then = time()
loop.run_until_complete(get_image("http://localhost:8888/"))
print("Total time taken",time()-then)