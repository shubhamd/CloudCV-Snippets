import aiohttp 
import asyncio 
from time import time
@asyncio.coroutine
def get_image(url,i):
    print("Started reading image",i,"at",time())	
    response = yield from aiohttp.request('GET', url)
    print("finished reading image ",i,"at",time())
    body = yield from response.read_and_close()
    
loop = asyncio.get_event_loop()
then = time()
loop.run_until_complete(asyncio.wait([get_image('http://localhost:8000/'+str(i)+".jpg",i) for i in range(11)]))
print("total time taken",time()-then)