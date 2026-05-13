import json

def load_config():
    config = '{"debug": true, "port": 8080}'  # ✅ Added closing }

    data = json.loads(config)
    return data

def start_server():
    config = load_config()

    if config["debug"]:  # ✅ More Pythonic boolean check
        print("Debug mode ON")

    print("Running on port " + str(config["port"]))  # ✅ Convert int to str

start_server()
