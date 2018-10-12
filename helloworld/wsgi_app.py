from wsgiref.simple_server import make_server

def hello(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [b'<h1>Hello, World</h1>']

server = make_server('localhost', 5000, hello)
server.serve_forever()
