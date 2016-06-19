#coding=utf8
#__author__ = 'wanghf'


import tornado.web
import tornado.httpserver


class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        #访问数据库验证
        user=dict(
            id='1',
            name='wanghaifei',
            passwrd='124',
            viewname='王海飞',
            is_admin=True
        ) #self.db.get('select * from usrs  where username=%s  and passwrd=%s',self.get_argument("username"),self.get_argument("passwrd"))

        if not user:
            self.render("login.html",error="用户名或密码  错误")
        else:
            self.set_secure_cookie("userid", str(user['id']))
            self.redirect(self.get_argument("next", "/main"))