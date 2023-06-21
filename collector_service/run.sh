#!/bin/bash
root_path="/home/nishma/SoftwareEngineering/Nishma/fastapi_projects/log_collector"
source "$root_path"/venv/bin/activate
python "$root_path"/collector_service/log_collector.py $root_path/collector_service/config/config.json