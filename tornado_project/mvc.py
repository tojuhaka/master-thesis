import tornado.ioloop
from tornado import websocket


class Model(websocket.WebSocketHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.counter = 0

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        self.counter += 1
        self.write_message(u"State changed: " + str(self.counter))


def make_app():
    return tornado.web.Application([
        (r"/websocket", Model),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
