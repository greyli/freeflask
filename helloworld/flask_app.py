from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, World!'

# $ export FLASK_APP=flask_app
# $ flask run
# http://localhost:5000