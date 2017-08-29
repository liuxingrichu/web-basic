#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print('get')
        u = self.get_argument('user')
        e = self.get_argument('email')
        p = self.get_argument('pwd')
        if u == 'Tom' and e == '163' and p == '123':
            self.write('OK')
        else:
            self.write('go out')

    def post(self):
        print('post')
        u = self.get_argument('user')
        e = self.get_argument('email')
        p = self.get_argument('pwd')
        print(u, e, p)
        self.write('POST')


application = tornado.web.Application([
    (r'/index', MainHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
