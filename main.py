#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
from tornado.options import define, options

import json
import os.path

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


cone = []

import sendkey

class SocketHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, application, request, **kwargs):
        tornado.websocket.WebSocketHandler.__init__(self, application, request, **kwargs)
        self.mc = MouseController()

    def open(self):
        if self not in cone:
            cone.append(self)
        print "-------------------"
        print "connected"
        print cone
        print "--------------------"


    def on_close(self):
        if self in cone:
            cone.remove(self)
        print "------------------"
        print "dis-connected"
        print cone
        print "-------------------"

    def on_message(self, message):
        js = json.loads(message)
        print '[WS]command: ' + js['command']
        print message

        if (js['command'] == 'PING'):
            ret = {'command': 'PONG'}
            self.write_message(json.dumps(ret))
            return

        elif (js['command'] == 'MOUSE_MOVE'):
            payload = js['payload']
            self.mc.move(payload)

        elif (js['command'] == 'MOUSE_DOWN'):
            payload = js['payload']
            self.mc.down(payload)

        elif (js['command'] == 'MOUSE_UP'):
            payload = js['payload']
            self.mc.up(payload)

        elif (js['command'] == 'MOUSE_WHEEL'):
            payload = js['payload']
            self.mc.wheel(payload)

        elif (js['command'] == 'KEY_DOWN'):
            payload = js['payload']
            sendkey.key_down(payload['keycode'])

        elif (js['command'] == 'KEY_UP'):
            payload = js['payload']
            sendkey.key_up(payload['keycode'])

        elif (js['command'] == 'SCREEN'):
            payload = js['payload']
            width  = payload['width']  if 'width'  in payload else 400
            height = payload['height'] if 'height' in payload else 300
            from pyscreenshot import grab
            from PIL import Image
            im = grab(backend=None)
            im.thumbnail((width, height), Image.ANTIALIAS)
            btb64 = BufferToBase64(self)
            im.save(btb64, "WEBP")
            b64 = btb64.get()

            ret = {
                'command': 'SCREEN',
                'payload': b64
            }
            self.write_message(json.dumps(ret))
            return

import io
class BufferToBase64(io.IOBase):
    def __init__(self, *args, **kwards):
        super(BufferToBase64, self).__init__(args, kwards)
        self.buf = []

    def write(self, bytes):
        self.buf.extend(bytes)

    def get(self):
        s = ''.join(self.buf)
        import base64
        b64 = base64.b64encode(s)
        return b64

    def close(self, *args, **kwargs):
        self.buf = []
        return super(BufferToBase64, self).close(args, kwargs)


class MouseController():
    def __init__(self):
        import ctypes
        user32 = ctypes.windll.user32
        self.screen = (self.width, self.height) = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        import mouse
        self.m = mouse.Mouse()

    def move(self, payload):
        p = self.xy2pos(payload)
        self.m.move_mouse(p)

    def down(self, payload):
        p = self.xy2pos(payload)
        b = self.button2text(payload)
        self.m.press_button(p, b, False)

    def up(self, payload):
        p = self.xy2pos(payload)
        b = self.button2text(payload)
        self.m.press_button(p, b, True)

    def wheel(self, payload):
        p = self.xy2pos(payload)
        d = payload['delta']
        self.m.wheel(d)

    def xy2pos(self, xy):
        return (xy['x'] * self.screen[0]), (xy['y'] * self.screen[1])

    def button2text(self, payload):
        button = payload['button']
        return 'right' if button == 2 else 'middle' if button == 1 else 'left'

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/websocket", SocketHandler),

            # to avoid templates
            (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "./img/"}),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static/"}),
            (r"/robots.txt", tornado.web.StaticFileHandler, {"path": "./robots.txt"}),
        ],
        template_path=os.path.join(os.getcwd(),  "www/templates"),
        static_path=os.path.join(os.getcwd(),  "www/static"),
        debug=True,

    )

    print "server starting at PORT=%d" % options.port

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
