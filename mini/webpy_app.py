import web

urls = (
    '/', 'hello'
)

class hello:
    def GET(self):
        return 'Hello, World!'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

# $ python webpy_app.py
