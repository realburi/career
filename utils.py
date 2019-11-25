def csv_fixer():
	import csv
	with open('data.csv', 'r', encoding="utf-8") as csv_data:
		data = csv.reader(csv_data, delimiter=',')
		result = [x for x in data if len(x) != 0]
		return result

def csv_fixer_1():
	import csv
	with open('real_data.csv', 'r', encoding="utf-8") as csv_data:
		data = csv.reader(csv_data, delimiter=',')
		result = [x for x in data if len(x) != 0]
		return result


def phone_check(number):
	import csv
	with open('data.csv','r', encoding="utf-8") as csv_data:
		data = csv.reader(csv_data, delimiter=',')
		result = [x for x in data]
		a = [x for x in result if number in x]
		return len(a) != 0

def del_row(number):
	import csv
	with open('data.csv','r', encoding="utf-8") as csv_data:
		data = csv.reader(csv_data, delimiter=',')
		_data = [x for x in data]
		result = {'real' : [x for x in _data if number not in x and len(x) != 0], 'fake' : [x for x in _data if number in x and len(x) != 0]}
		return result 

def remainder_row(number):
	import csv
	data = del_row(number)['real']
	open('data.csv', 'w').close()
	with open('data.csv','a',encoding='utf-8') as csv_data:
		data_writer = csv.writer(csv_data, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL) 
		result = [x for x in data if len(x) != 0]
		for x in result:
			data_writer.writerow(x)

def else_row(number):
	import csv
	data = del_row(number)['fake']
	with open('real_data.csv','a',encoding='utf-8') as csv_data:
		data_writer = csv.writer(csv_data, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL) 
		result = [x for x in data if len(x) != 0]
		for x in result:
			data_writer.writerow(x)
		return result
print(else_row('95715468'))