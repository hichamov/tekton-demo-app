import http.server
import random
from prometheus_client import start_http_server
from prometheus_client import Counter

# Adding counters of requests and exceptions
REQUESTS = Counter('hello_worlds_total', 'Hello Worlds requested.')
#EXCEPTIONS = Counter('hello_world_exceptions_total', 'Exceptions serving Hello World.')

class MyHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            REQUESTS.inc()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Test From Tekton 4 !!!")

if __name__ == "__main__":
        start_http_server(8000)
        server = http.server.HTTPServer(('0.0.0.0', 8001), MyHandler)
        server.serve_forever()
