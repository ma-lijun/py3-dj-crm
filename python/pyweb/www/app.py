__author__ = 'ma_lijun'

import logging; logging.basicConfig(level=logging.INFO)

import  asyncio,os,json,time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>forum</h1>', content_type='text/html', charset='UTF-8')#新增加编码，确切为编码类型html

asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9002)
    logging.info('server started at http://127.0.0.1:9001...')
    return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
