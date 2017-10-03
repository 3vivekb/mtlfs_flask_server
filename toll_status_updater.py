import json
import datetime

TTL = 300
last_updated = int(datetime.datetime.now().timestamp())

file_name = "../live_toll.json"

with open(file_name) as data_file:
	datum = json.load(data_file)

data = {}
data['facilities'] = datum
for facility in data['facilities']:
	facility['algorithm_mode'] = facility.pop('Algorithm_Mode')
	facility['message_module'] = facility.pop('Message_Module')
	facility['pricing_module'] = facility.pop('Pricing_Module')
	facility['interval_starting'] = int(facility.pop('Interval_Starting')/1000)
	facility['facility_id'] = facility.pop('Plaza_Name')
	del facility['User']
	del facility['biCalSeqID']
live_toll = {}
live_toll['data'] = data

live_toll['last_updated'] = last_updated
live_toll['ttl'] = TTL

with open('static/toll_status.json', 'w') as f:
	json.dump(live_toll, f, ensure_ascii=False)
