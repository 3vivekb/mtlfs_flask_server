import json
import datetime

TTL = 300
last_updated = int(datetime.datetime.now().timestamp())

file_list = ["mtlfs.json", "toll_facility.json", 'toll_authority_info.json',
'general_toll_info.json', 'toll_destination.json', 'toll_periods.json']

for file in file_list:
	file_name = str('../mtlfs/' + file)
	with open(file_name) as data_file:
		data = json.load(data_file)

	data['last_updated'] = last_updated
	data['ttl'] = TTL

	with open('static/' + file, 'w') as f:
		json.dump(data, f, ensure_ascii=False)

geom_list = ["facility_geom.json", "gantry_geom.json", "toll_signs_geom.json"]

for file in file_list:
	file_name = str('../mtlfs/' + file)
	with open(file_name) as data_file:
		data = json.load(data_file)
	with open('static/' + file, 'w') as f:
		json.dump(data, f, ensure_ascii=False)

