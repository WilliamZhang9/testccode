import json

def load_config():
    config_str = '{"debug": true, "port": 8080}'
    config = json.loads(config_str)
    if config["debug"]:
        print("Debug mode ON")
    print("Running on port " + str(config["port"]))

if __name__ == "__main__":
    load_config()
