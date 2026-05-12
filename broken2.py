import json

# FIX: Added missing closing brace '}' to the JSON string
config_str = '{"debug": true, "port": 8080}'
config = json.loads(config_str)

if config["debug"]:
    print("Debug mode ON")

# FIX: Wrapped integer in str() to allow concatenation with string
print("Running on port " + str(config["port"]))
