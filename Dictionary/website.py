from flask import Flask, render_template, request

app = Flask(__name__)

a = {"found":True,"citypayer":False,"vatpayer":True,"receiptFound":False,"lastReceiptDate":None,"vatpayerRegisteredDate":"2010-08-16","name":"АРГОДРИС"}

@app.route('/')
def index():
	return a

if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)