import json
import socket
import sys
import shelve

s = socket.socket()

shelf = shelve.open('/home/nishma/SoftwareEngineering/Nishma/fastapi_projects/log_collector/collector_service/files/count_data')
count = shelf.get('count') or 0



def get_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config


def file_writer(file_path, message):
    global count
    with open(file_path, "a") as file:
        content = file.write(message.decode() + "\n")
        print(message.decode())
        count += 1
    return count

def get_next_file(file_path):
    file_index = file_path.split(".")[0].split("/")[-1].split("_")[-1]
    return int(file_index) + 1



def log_collector_service(config):
    
    global count
    s.bind(("localhost", config.get("port")))
    s.listen(5)
    client_socket, address =  s.accept()
    
    file_path = shelf.get("file") or "/home/nishma/SoftwareEngineering/Nishma/fastapi_projects/log_collector/collector_service/files/log_1.txt"
    while True:
        message = client_socket.recv(1024)
        if not message:
            continue
        line_count = file_writer(file_path, message)
        shelf["count"] = line_count
        # shelf.sync()

        if line_count == config.get("max_lines"):
            count = 0            
            next_index = get_next_file(file_path)
            file_path = f"/home/nishma/SoftwareEngineering/Nishma/fastapi_projects/log_collector/collector_service/files/log_{next_index}.txt"
            shelf["file"] = file_path
            # shelf.sync()


def main():
    config_path = sys.argv[1]
    config = get_config(config_path)
    log_collector_service(config)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("syncing shelve on keyboard interrupt")
        shelf.sync()
    