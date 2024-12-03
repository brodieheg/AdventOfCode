import requests
import json

def getInputData(day):
    res = requests.get("https://adventofcode.com/2024/day/{day}/input")
    return json.loads(res.text)
