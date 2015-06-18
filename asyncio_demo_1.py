import aiohttp 
import asyncio 
from time import time
from os import listdir 

images = listdir("/home/shubham/Pictures/source")
# images = images[:2]
print(len(images))
url = "http://localhost:8000/"
@asyncio.coroutine
def get_images(*args, **kwargs):
	
	response = yield from aiohttp.request('GET', *args, **kwargs)
	


loop = asyncio.get_event_loop()
f = asyncio.wait([get_images(url+i) for i in images])
then = time()
loop.run_until_complete(f)
print("Total time taken",time()-then)