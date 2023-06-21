from pydantic import BaseModel


class Config(BaseModel):
    service_name: str
    port: int
    max_lines: int = 100