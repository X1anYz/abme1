from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
	link = "<h1>歡迎進入張佑先的網站首頁</h1>"
	link += "<a href=/about>關於佑先</a><hr>"
	return link

@app.route("/mis")
def course():
	return "<h1>資訊管理導論</h1><a href=/>回到網站首頁<a>"

@app.route("/about")
def about():
	return render_template("sg.html")


if __name__ == "__main__":
	app.run()