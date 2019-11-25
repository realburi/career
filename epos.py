import requests as rq 

url = "http://info.ebarimt.mn/rest/merchant/info?"

data = {}
for x in range(5186500,5186580,1):
	params = {"regno" : x}
	a = rq.get(url,params=params).json()
	if a['found'] == True:
		data.update({x : a['name']})

print(data)
