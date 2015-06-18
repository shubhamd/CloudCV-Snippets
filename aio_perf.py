import asyncio
from aiohttp import web 

@asyncio.coroutine
def hello(request):
	return web.Response(body="hello world!!")

app = web.Application()
app.router.add_route('GET','/',hello)