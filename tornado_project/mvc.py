import tornado.ioloop
from tornado import websocket


class Model(websocket.WebSocketHandler):
    counter = 0

    def check_origin(self, origin):
        return True

    def increase(self):
        self.counter += 1
        self.write_message(str(self.counter))

    def decrease(self):
        self.counter -= 1

    def get_value(self):
        return self.counter

    def on_message(self, message):
        {"get": self.get_value,
         "increase": self.increase,
         "decrease": self.decrease}[message]()

        self.write_message(str(self.get_value()))


def make_app():
    return tornado.web.Application([
        (r"/model", Model),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
