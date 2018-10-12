from flask import Flask, MethodView

app = Flask(__name__)

# Method 1
@app.route('/foo')
def foo():
	return 'Hello, Foo!'


# Method 2
def bar():
	return 'Hello, Bar!'

app.add_url_rule('/bar', bar)


# Method 3
class Baz(MethodView):

	def get():
		return 'Hello, Baz!'

app.add_url_rule('/baz', Baz.as_view('baz'))

# $ flask run
