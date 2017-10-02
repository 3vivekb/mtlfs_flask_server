from flask import Flask, json
app = Flask(__name__)

@app.route('/')
def default():
	return app.send_static_file('mtlfs.json')

@app.route('/mtlfs/about')
def about():
	return 'Check out https://github.com/vta/Managed-and-Tolled-Lanes-Feed-Specification/ or the mtlfs.json page.'

@app.route('/mtlfs/mtlfs.json')
def mtlfs():
	return app.send_static_file('mtlfs.json')

@app.route('/mtlfs/general_toll_info.json')
def general_toll_info():
	return app.send_static_file('general_toll_info.json')

@app.route('/mtlfs/toll_authority_info.json')
def toll_authority_info():
	return app.send_static_file('toll_authority_info.json')

@app.route('/mtlfs/toll_destination.json')
def toll_destination():
	return app.send_static_file('toll_destination.json')

@app.route('/mtlfs/toll_facility.json')
def toll_facility():
	return app.send_static_file('toll_facility.json')

@app.route('/mtlfs/toll_periods.json')
def toll_periods():
	return app.send_static_file('toll_periods.json')

@app.route('/mtlfs/toll_status.json')
def toll_status():
	return app.send_static_file('toll_status.json')

@app.route('/mtlfs/toll_signs_geom.json')
def toll_signs():
	return app.send_static_file('../mtlfs/toll_signs_geom.json')

@app.route('/mtlfs/gantry_geom.json')
def gant():
	return app.send_static_file('../mtlfs/gantry_geom.json')

@app.route('/mtlfs/facility_geom.json')
def facility_geom():
	return app.send_static_file('../mtlfs/facility_geom.json')