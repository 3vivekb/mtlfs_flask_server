# mtlfs_flask_server

This is a simple flask server meant to serve up the [mtlfs](https://github.com/vta/mtlfs) in the proper [schema](https://github.com/vta/Managed-and-Tolled-Lanes-Feed-Specification).  

Raw data is currently being received with the [express lanes api](https://github.com/vta/expresslanes-api) API (on the doubler branch) and writes it to disk as well as triggers an update which updates the data served by the flask server.

Find the updated data with the [discovery json](https://mtlfs.vta.org/mtlfs/mtlfs.json) or directly at the [toll status json](https://mtlfs.vta.org/mtlfs/toll_status.json).
