from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/') #This is the root
def index():
	return render_template('index.html')

@app.route('/ninjas')
def ninja():
	return render_template('/ninja.html')

@app.route('/dojos/new')
def newNinja():
	return render_template('/new.html')

app.run(debug=True)