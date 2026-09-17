def process(data):
    result = []
    for i in range(len(data)):
        if data[i]["status"] == "active":
            if data[i]["value"] > 0:
                x = data[i]["value"] * 1.1
                if data[i]["type"] == "A":
                    x = x * 2
                result.append({"id": data[i]["id"], "final": x})
            else:
                print("skipping " + str(data[i]["id"]))
    return result

d = [
    {"id": 1, "status": "active", "value": 10, "type": "A"},
    {"id": 2, "status": "inactive", "value": 5, "type": "B"},
    {"id": 3, "status": "active", "value": -2, "type": "A"},
    {"id": 4, "status": "active", "value": 7, "type": "B"},
]

print(process(d))
