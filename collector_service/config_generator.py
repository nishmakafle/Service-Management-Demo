import json
from library.db_connection import database


def serialize(obj):
    obj['_id'] = str(obj.get('_id'))
    return obj


def get_config_data(service_name):
    data = database.config.find_one({'service_name': service_name})
    result = {
        "port": data['port'],
        "max_lines": data['max_lines'],
    }
    return result


def file_generate(data, file_path):   
    with open(file_path, "w") as file:
        content = json.dump(data, file)      


def db_data_collector(): 
    file_path = "collector_service/config/config.json"
    service_name = "log_collector"
    data = get_config_data(service_name)
    file_generate(data, file_path)

def main(): 
    db_data_collector(data)


if __name__ == '__main__':
    main()