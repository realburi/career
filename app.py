from flask import Flask, render_template, url_for, request
import csv
from utils import *

app = Flask(__name__)

@app.route('/')
def index():
	if request.method == "GET":
		return render_template('index.html', data=csv_fixer())
	elif request.method == "POST":
		return request.form

@app.route('/timetable')
def timetable():
	return render_template('time.html')

@app.route('/redirect', methods=['POST'])
def red():
	if request.method == 'POST':
		result = [x for x in request.form.values() if x != '']
		with open('data.csv', mode='a', encoding='utf-8', newline='') as data_file:
			data_writer = csv.writer(data_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
			data_writer.writerow(result)
		return render_template('success.html')

@app.route('/confirm', methods=['GET','POST'])
def confirm():
	if request.method == "POST":
		phone_number = request.form[" \u0425\u043e\u043b\u0431\u043e\u0433\u0434\u043e\u0445 \u0443\u0442\u0430\u0441"]
		else_row(phone_number)
		remainder_row(phone_number)
		return render_template('success.html')
	elif request.method == "GET":
		return 'Hi!'
		
@app.route('/delete',methods=['POST'])
def delete():
	phone_number = request.form[" \u0425\u043e\u043b\u0431\u043e\u0433\u0434\u043e\u0445 \u0443\u0442\u0430\u0441"]
	remainder_row(phone_number)
	return render_template('success.html')

@app.route('/meeters', methods=['GET'])
def meeters():
	if request.method == "GET":
		return render_template('meeters.html', data=csv_fixer_1())


@app.route('/french', methods=['GET','POST'])
def french():
	if request.method == "GET":
		return render_template('french.html')
	elif request.method == "POST":
		return request.form

if __name__=='__main__':
	    app.run(host= '0.0.0.0', port=9000, debug=True)
