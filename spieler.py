# B. Ege

import os
import csv
import json

csvFilePath = "./spieler.txt"
jsonFilePath = "./spieler.json"

if os.path.exists(jsonFilePath):
    os.remove(jsonFilePath)

output_dict = {"persons": [], "data": []}


with open(csvFilePath, "r", encoding="utf-8") as csvFile:
    for line in csv.reader(csvFile, delimiter=";"):
        output_dict["persons"].append({"sensorId": line[1], "spielerId": line[2]})
        output_dict["data"].append(
            {"sensorId": line[1], "x": line[6], "y": line[7], "z": line[8]}
        )

with open(jsonFilePath, "a", encoding="utf-8") as jsonFile:
    json.dump(output_dict, jsonFile, indent=4, sort_keys=True)
    print("json file has been created successfully!")


