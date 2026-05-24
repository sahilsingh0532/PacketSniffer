from flask import Flask, request
from ui import stylish_ui

app = Flask(__name__)

@app.route("/")
def hello_world():
	content = """
	<h1>Free WiFi</h1>
	<form action="/login" method="post">
		Username:<input type="text" name="username">
		Password:<input type="password" name="password">
		<input type="submit" value="login">
	</form>
	"""
	return stylish_ui(content)
	
@app.route("/login", methods=["POST"])
def login():
	user = request.form.get("username")
	return f"successfully logged in as <b>{user}</b>"
	
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80)
	
