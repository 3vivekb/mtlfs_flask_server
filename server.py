from flask import Flask, json
app = Flask(__name__)

@app.route('/')
def default():
	return app.send_static_file('mtlfs.json')

@app.route('/about')
def about():
	return 'Check out https://github.com/vta/Managed-and-Tolled-Lanes-Feed-Specification/ or the mtlfs.json page.'

@app.route('/mtlfs.json')
def mtlfs():
	return app.send_static_file('mtlfs.json')

@app.route('/general_toll_info.json')
def general_toll_info():
	return app.send_static_file('general_toll_info.json')


@app.route('/toll_authority_info.json')
def toll_authority_info():
	return app.send_static_file('toll_authority_info.json')

@app.route('/toll_destination.json')
def toll_destination():
	return app.send_static_file('toll_destination.json')

@app.route('/toll_facility.json')
def toll_facility():
	return app.send_static_file('toll_facility.json')

@app.route('/toll_periods.json')
def toll_periods():
	return app.send_static_file('toll_periods.json')

@app.route('/toll_status.json')
def toll_status():
	return app.send_static_file('toll_status.json')


@app.route('/toll_signs_geom.json')
def toll_signs():
	return app.send_static_file('../mtlfs/toll_signs_geom.json')

@app.route('/gantry_geom.json')
def gant():
	return app.send_static_file('../mtlfs/gantry_geom.json')

@app.route('/facility_geom.json')
def facility_geom():
	return app.send_static_file('../mtlfs/facility_geom.json')
if __name__ == '__main__':
    app.run(debug=True)
