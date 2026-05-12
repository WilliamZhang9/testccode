import json

config_json = '{"port": 8080, "debug": true}'
config = json.loads(config_json)

if config["debug"]:
    print("Debug mode ON")

print("Running on port " + str(config["port"]))
