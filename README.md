# mtlfs_flask_server

This is a simple flask server meant to serve up the [mtlfs](https://github.com/vta/mtlfs).  

Raw data is currently being received with the [express lanes api](https://github.com/vta/expresslanes-api) and writes it to disk as well as triggers an update
which updates the data served by the flask server.

Find the updated data with the [discovery json](https://mtlfs.vta.org/mtlfs/mtlfs.json) or directly at the [toll status json](https://mtlfs.vta.org/mtlfs/toll_status.json).
