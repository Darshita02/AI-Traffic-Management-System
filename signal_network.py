import json
import time

while True:

    with open("traffic_state.json") as f:
        data=json.load(f)

    traffic=data["traffic"]

    signals=[]

    for area in traffic:
        for s in traffic[area]:
            signals.append(f"{area}-{s}")

    network={}

    for s in signals:
        network[s]=[x for x in signals if x!=s]

    data["signal_network"]=network

    with open("traffic_state.json","w") as f:
        json.dump(data,f,indent=2)

    print("Signal network updated")

    time.sleep(3)
