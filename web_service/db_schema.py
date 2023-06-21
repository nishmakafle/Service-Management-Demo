from pydantic import BaseModel, validator
from pydantic_validators import UniqueValidator
from typing import List

class Config(BaseModel):
    service_name: str
    port : int
    max_lines : int

    @validator('service_name')
    def check_unique_name(cls, service_name):
        validator = UniqueValidator(queryset=[service.service_name for service in services])
        validator(service_name)
        return service_name
