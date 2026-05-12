import json

config_json = '{"debug": "on", "port": 8080}'
config = json.loads(config_json)

if config["debug"] == "on":
    print("Debug mode ON")

print("Running on port " + str(config["port"]))
