#coding=utf8
import base64,uuid

__author__ = 'wanghf01'


import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

#测试
if __name__ == "__main__":

    app = make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()
