import json

def load_config():
    config = '{"debug": true, "port": 8080'  # ❌ missing closing }

    data = json.loads(config)
    return data

def start_server():
    config = load_config()

    if config["debug"] == True:
        print("Debug mode ON")

    print("Running on port " + config["port"])  # ❌ int + str

start_server()
