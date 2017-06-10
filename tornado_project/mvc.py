import tornado.ioloop
from tornado import websocket


class Model(websocket.WebSocketHandler):
    counter = 0

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")

    def on_close(self):
        print("WebSocket closed")

    def increase(self):
        self.counter += 1
        self.write_message(str(self.counter))

    def decrease(self):
        self.counter -= 1

    def on_message(self, message):
        {"get": lambda: True,
         "increase": self.increase,
         "decrease": self.decrease}[message]()

        self.write_message(str(self.counter))


def make_app():
    return tornado.web.Application([
        (r"/model", Model),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
