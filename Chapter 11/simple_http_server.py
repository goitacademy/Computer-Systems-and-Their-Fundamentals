from threading import Thread
from time import sleep
from http import client
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, world!")

    def do_POST(self):
        pass


httpd = HTTPServer(("localhost", 8001), SimpleHTTPRequestHandler)
server = Thread(target=httpd.serve_forever)
server.start()
sleep(0.5)

h1 = client.HTTPConnection("localhost", 8001)
h1.request("GET", "/")

res = h1.getresponse()
print(res.status, res.reason)
data = res.read()
print(data)

httpd.shutdown()
