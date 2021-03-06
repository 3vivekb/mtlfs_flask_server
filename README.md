# mtlfs_flask_server

This is a simple flask server meant to be an API for the VTA [mtlfs](https://github.com/vta/mtlfs) in the proper [schema](https://github.com/vta/Managed-and-Tolled-Lanes-Feed-Specification).  

Raw data is currently being received with the [Express Lanes Api Receiver](https://github.com/vta/expresslanes-api) which writes the data to disk and triggers an update to the data served by the flask server.

The Flask server uses a combination of the dynamic data from the receiver and the static descriptive json data in our [mtlfs repo](https://github.com/vta/mtlfs) to produce output for the api.

See an example with the [discovery json](https://mtlfs.vta.org/mtlfs/mtlfs.json) or get the dynamic data directly at the [toll status json](https://mtlfs.vta.org/mtlfs/toll_status.json).


## How to Run in Dev:
1. Get the [mtlfs](https://github.com/vta/mtlfs) in a directory alongside this repo
1. Clone this repo.
1. Install the necessary packages(`pip install flask`) to your Python 3 environment.
1. Add environment variable `export FLASK_APP=server.py`
1. Turn on debug mode `export FLASK_DEBUG=1`
1. Run server `flask run`
1. View at 127.0.0.1:5000

## Production Mode Details:
1. [This guide to get started](https://www.matthealy.com.au/blog/post/deploying-flask-to-amazon-web-services-ec2/)
1. Use nginx
1. Use gunicorn to run `gunicorn --bind 0.0.0.0:8000 server:app`
1. Run the express lanes api with node.
1. Serve up both gunicorn and the node server with supervisorctl
