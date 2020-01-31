import tornado.ioloop
import tornado.web
from predictionHandler import PredictionHandler

def make_app():
    return tornado.web.Application([
        (r"/get_occupied_prediction", PredictionHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(6543)
    tornado.ioloop.IOLoop.current().start()
