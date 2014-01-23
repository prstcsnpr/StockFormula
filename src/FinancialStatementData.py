# -*- coding: utf-8 -*-

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print ''

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()