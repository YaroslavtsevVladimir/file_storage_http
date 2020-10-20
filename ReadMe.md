# Local file storage 

## Introduction
This is a local file storage with HTTP API.
You can download, upload and delete files using GET, POST and DELETE methods.
When you upload a file, the name will be replaced with a hash.
The app creates a `store` folder in your home directory, and when you upload a file,
the app will create a new folder named by the first two symbols of the file hash.

## How to use
After cloning the repo, you need to add and activate python virtual environment:
- `python3 -m venv venv`
- `pip install -r requirements.txt`
- `source venv/bin/activate`

#### How to run
You can run it as a Flask app using the following command:
- `python app.py`

Or you can run it as a daemon on your system.

There are to options:
1) Use this command to run: `sudo nohup flask run > log.txt 2>&1`, after using this command you will get a PID. 
To stop a daemon use `kill -9 PID`.
2) Run `run_server` bash script.
 
##### How bash script works
- It copies `file_storage.service` to `/etc/systemd/system/` 
- It allows to run, stop and check the status of a daemon.

For the first you need to update `User`, `Working directory` and `ExecStart` fields in the `file_storage.service` file. 
Replace `<Chuck Norris>` with your current user and `<path to project>` with your path to this repo:
- to start a daemon: `./run_server start`
- to stop a daemon: `./run_server stop`
- to check the status: `./run_server status`

The server listens on port 5000 by default. [http://localhost:5000/](http://localhost:5000/).

After running the server, you can use the web-interface or curl:
![](./images/Screenshot%20from%202020-10-19%2017-19-19.png)

![](./images/Screenshot%20from%202020-10-19%2017-19-29.png)

![](./images/terminal.png)
