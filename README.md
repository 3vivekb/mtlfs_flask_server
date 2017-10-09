# mtlfs_flask_server

This is a simple flask server meant to serve up the [mtlfs](https://github.com/vta/mtlfs) in the proper [schema](https://github.com/vta/Managed-and-Tolled-Lanes-Feed-Specification).  

Raw data is currently being received with the [express lanes api](https://github.com/vta/expresslanes-api) API (on the doubler branch) and writes it to disk as well as triggers an update which updates the data served by the flask server.

Find the updated data with the [discovery json](https://mtlfs.vta.org/mtlfs/mtlfs.json) or directly at the [toll status json](https://mtlfs.vta.org/mtlfs/toll_status.json).


## How to Run in Dev:
1. Get the [mtlfs](https://github.com/vta/mtlfs) in a directory alongside this repo
1. Clone this repo.
1. Install the necessary packages(`pip install flask`) to your Python 3 environment.
1. Add environment variable `export FLASK_APP=server.py`
1. Turn on debug mode `export FLASK_DEBUG=1`
1. Run server `flask run`

## Production Mode Details:
1. [This guide to get started](https://www.matthealy.com.au/blog/post/deploying-flask-to-amazon-web-services-ec2/)
1. Use nginx
1. Use gunicorn to run `gunicorn --bind 0.0.0.0:8000 server:app`
1. Run the express lanes api with node.
1. Serve up both gunicorn and the node server with supervisorctl
