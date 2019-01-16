import requests
import time
import json
from datetime import datetime as dt

server_ip = ['203.104.209.71', '203.104.209.87', '125.6.184.215', '203.104.209.183', '203.104.209.150', '203.104.209.134', '203.104.209.167', '203.104.209.199', '125.6.189.7', '125.6.189.39', '125.6.189.71', '125.6.189.103', '125.6.189.135','125.6.189.167', '125.6.189.215', '125.6.189.247', '203.104.209.23', '203.104.209.39', '203.104.209.55', '203.104.209.102']
server_name = ['Yokosuka', 'Kure', 'Sasebo', 'Maizuru', 'Ominato', 'Truk', 'Lingga', 'Rabaul', 'Shortland', 'Buin', 'Tawi-tawi', 'Plau', 'Brunei', 'Hitokappu', 'Paramushir', 'Sukumo', 'Kanoya', 'Iwagawa', 'Saiki', 'Hashirajima']
server_status = ["True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True"]
post_url = "(discord webhook URL)"

while (1):
	for i in range(20):
		server = "http://" + server_ip[i] + "/favicon.icon"
		try:
			r = requests.get(server, timeout=3)
		except requests.exceptions.ConnectTimeout:
			status = "False"
		else:
			status = "True"
		now = dt.now()
		status_log = server_name[i].rjust(11) + " : " + status + " " + now.strftime("%H:%M:%S") 
		if(status == "True"):
			status_log = status_log +  " " + str(round(r.elapsed.total_seconds() * 1000, 2)) + "ms"
		print(status_log)

		if(server_status[i] != status):
			if(status == "True"):
				messege = ":chart_with_upwards_trend:" + server_name[i] + " : online @ " + now.strftime("%H:%M:%S")
			else:
				messege = ":chart_with_downwards_trend:" + server_name[i] + " : offline @ " + now.strftime("%H:%M:%S")
			response = requests.post(
			post_url,
			json.dumps({
				"username" : "Neko Checker",
				"content": messege
			}),
			headers = {"Content-Type" : "application/json"}
			)

		server_status[i] = status
		time.sleep(1)
	print("")
	time.sleep(10)

