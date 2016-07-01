#coding=utf8
#__author__ = 'wanghf'
import os

import tornado.web
import tornado.httpserver
from tornado.options import define, options
import torndb

from handler.UserHandler import LoginHandler, LogoutHandler
from handler.cache import CacheHandler
from modules.view import EntryModule

define("port", default=8889, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="recomm database host")
define("mysql_database", default="recomm", help="recomm database name")
define("mysql_user", default="recomm", help="recomm database user")
define("mysql_password", default="1234", help="1234 database password")


# def administrator(method):
#     """Decorate with this method to restrict to site admins."""
#     @functools.wraps(method)
#     def wrapper(self, *args, **kwargs):
#         if not self.current_user:
#             if self.request.method == "GET":
#                 self.redirect(self.get_login_url())
#                 return
#             raise tornado.web.HTTPError(403)
#         elif not self.current_user.administrator:
#             if self.request.method == "GET":
#                 self.redirect("/")
#                 return
#             raise tornado.web.HTTPError(403)
#         else:
#             return method(self, *args, **kwargs)
#     return wrapper

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
            return self.get_secure_cookie("userid")
         #self.db.get("SELECT * FROM authors WHERE id = %s", int(user_id))




class IndexHandler(BaseHandler):
    def get(self):
        self.render("login.html")






class HomeHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        user1=dict(
            id='1',
            name='wanghaifei',
            passwrd='124',
            viewname='王海飞',
            is_admin=True
        )
        user=CacheHandler.get(self.get_secure_cookie("userid"))

        self.render("home.html", user=user)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/login",LoginHandler),
            (r"/logout",LogoutHandler),
            (r"/main",HomeHandler)
        ]
        settings = dict(
            title=u"基金智能推荐",
            template_path=os.path.join(os.path.dirname(__file__), "../webapp/templates"),
            static_path=os.path.join(os.path.dirname(__file__), "../webapp/static"),
            ui_modules={"Entry": EntryModule},
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/",

        )

        super(Application, self).__init__(handlers, **settings)
        # Have one global connection to the blog DB across all handlers
        # self.db = torndb.Connection(
        #     host=options.mysql_host, database=options.mysql_database,
        #     user=options.mysql_user, password=options.mysql_password)


def main():
    #解析传入的命令
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



if __name__ == '__main__':
    main()    
