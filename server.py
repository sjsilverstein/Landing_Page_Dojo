from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/') #This is the root
def index():
	return render_template('index.html')

app.run(debug=True)