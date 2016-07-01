#coding=utf8
#__author__ = 'wanghf'
import json

import tornado.web
import tornado.httpserver
from handler.cache import CacheHandler


class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        #访问数据库验证
        user=dict(
            id='1',
            name='wanghaifei',
            passwrd='123',
            viewname='王海飞',
            is_admin=True
        ) #self.db.get('select * from usrs  where username=%s  and passwrd=%s',self.get_argument("username"),self.get_argument("passwrd"))

        if self.get_argument('username')!=user['name'] or self.get_argument('passwrd')!=user['passwrd']:
            self.render("login.html", error="用户名或密码错误！")
            return


        if not user:
            self.render("login.html",error="用户名或密码  错误")
        else:
            self.set_secure_cookie("userid", str(user['id']))

            if not CacheHandler.cache.has_key(user['id']) :
                  CacheHandler.save(user['id'],user)

            self.redirect(self.get_argument("next", "/main"))


class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        CacheHandler.clear(self.get_secure_cookie("userid"))
        self.clear_cookie("userid")
        print(CacheHandler.list())
        self.redirect(self.get_argument("next", "/"))
