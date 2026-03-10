import json
import time

def calculate_time(lanes):

    total=sum(lanes.values())

    if total>120:
        return 60
    elif total>80:
        return 45
    elif total>40:
        return 30
    else:
        return 15

while True:

    with open("traffic_state.json") as f:
        data=json.load(f)

    traffic=data["traffic"]

    timing={}

    for area in traffic:

        timing[area]={}

        for signal in traffic[area]:

            lanes=traffic[area][signal]

            timing[area][signal]=calculate_time(lanes)

    data["signal_timing"]=timing

    with open("traffic_state.json","w") as f:
        json.dump(data,f,indent=2)

    print("Signal timing updated")

    time.sleep(2)
