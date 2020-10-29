from wsgiref.simple_server import make_server
from todo import app


def web_app(environment, response):
    status = "200 OK"
    headers = [("Content-type", "text/html; charset=utf-8")]
    response(status, headers)

    return [b"<strong> Hello World I just created my first WSGI</strong"]


with make_server("", 8090, app) as server:
    print(
        "Serving on port 8090...\nVisit http://127.0.0.1:8090\nTo kill server enter Control + C"
    )

    server.serve_forever()
