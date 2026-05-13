import json

def load_config():
    config = '{"debug": true, "port": 8080}'

    data = json.loads(config)
    return data

def start_server():
    config = load_config()

    if config["debug"] == True:
        print("Debug mode ON")

    print("Running on port " + str(config["port"])) 

start_server()
