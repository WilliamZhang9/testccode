import json

config_json = '{"debug": true, "port": 8080}'
config = json.loads(config_json)

if config["debug"]:
    print("Debug mode ON")

print("Running on port " + str(config["port"]))
