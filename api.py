
from SettingsModule.settings import user_collection_name, jwt_secret, mongo_db
from LoggingModule.logging import logger

import signal
from tornado.ioloop import IOLoop
import tornado.web
from LoginModule.login import Login
import coloredlogs
coloredlogs.install()
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        logger.debug("ewew")
        logger.error("Error occurred")
        print ("dsdsD")
        self.write("Hello, Feymen")

app_urls = [
        (r"/", MainHandler),
        (r"/login", Login),

    ]


def handle_signal(sig, frame):
    loop = IOLoop.instance()
    logger.info("stopping server dude")
    loop.add_callback(loop.stop)



if __name__ == "__main__":
    port = 8888
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
    app = tornado.web.Application(handlers=app_urls, db=mongo_db)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port)
    #asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    #AsyncIOMainLoop().install()
    #asyncio.get_event_loop().run_forever()
    logger.info("Application server started on %s"%port)
    #make_indexes()
    IOLoop.instance().start()