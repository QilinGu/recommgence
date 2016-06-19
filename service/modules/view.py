#coding=utf8
import tornado
import tornado.web

__author__ = 'wanghf'






class  User(object):

   def __init__(self,name,passwrd,viewname,is_admin):
    self.name=name
    self.passwrd=passwrd
    self.viewname=viewname
    self.is_admin=is_admin

class EntryModule(tornado.web.UIModule):
    def render(self, entry):
        print(entry['id'])
        return self.render_string("modules/user.html", entry=entry)