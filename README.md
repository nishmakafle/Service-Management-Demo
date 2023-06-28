## Python Service management Demo##

This is a simple python project which contains 2 services. One is collector service and another is web server. The collector service is written in python, has a run.sh script, and is run as a service. systemctl will start, stop and restart the service. 

The collector service is actually a network service that listen events on configured tcp port and stores them in a file. When the content of one file reaches to the configured limit, it then stores other events on different files.

 To run the collector service, we have a configuration file. The configuration file is generated and updated using web server service.

The web server is written using FastAPI framework which has some endpoints to generate configuration, run, start, restart and stop the collector service. FastAPI stores the configuration of the collector service to the Mongo DB. 

To run the service we have to make a service file in /etc/systemd/system/collector_service.service

```
[Unit]
Description=my collector service
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/path_from_your_root/.../collector_service/run.sh
[Install]
WantedBy=multi-user.target

```

TO run webserver

```
$ uvicorn web_service.main:app --reload
```


