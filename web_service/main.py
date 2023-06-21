from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from web_service.helpers import add_config
from collector_service.config_generator import db_data_collector
from web_service.models import Config


import subprocess




app = FastAPI()

@app.get("/")
async def home():
    return {"message":"Hello world"}


@app.post("/config_file")
async def save_configuration(request:Request):
    form_data = await request.form()
    data = {
        "port": form_data.get("port"),
        "max_lines": form_data.get("max_lines"),
        "service_name": form_data.get("service_name")
    }
    result = add_config(data)
    db_data_collector()
    
    return JSONResponse(status_code=200, content=result)

@app.post("/config")
def store_config(config: Config):
    data = config.dict()
    result = add_config(data)
    db_data_collector()
    
    return JSONResponse(status_code=200, content=result)


@app.get("/service_status")
def get_service_status(service_name: str):
    try:
        # Run the systemctl command to get the service status
        result = subprocess.run(['systemctl', 'is-active',service_name], capture_output=True, text=True)
        print(result)

        # Get the output and check the service status
        output = result.stdout.strip()
        if output == 'active':
            return 'running'
        elif output == 'failed':
            return 'failed'
        elif output == 'inactive':
            return 'Stopped'
        else:
            return 'unknown'
    except FileNotFoundError:
        return 'command not found'


@app.get('/service-tasks')
def service_tasks(service_name:str , task: str):
    
    result = subprocess.run(['systemctl',task, service_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Service '{service_name}' {task}ed successfully.")
    else:
        print(f"Failed to start service '{service_name}'. Error: {result.stderr}")



