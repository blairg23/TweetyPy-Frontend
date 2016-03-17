from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello_world():
	return 'Hello Buttsecks!'

@app.route('/profile/<post_id>')
def profile(post_id):
	return 'post_id is %s' % post_id

if __name__ == '__main__':
	app.run(debug=True)