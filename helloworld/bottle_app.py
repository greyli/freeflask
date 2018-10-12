from bottle import route, run

@route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
	run(host='localhost', port=8080)

# $ python bottle_app.py
# http://localhost:8080
