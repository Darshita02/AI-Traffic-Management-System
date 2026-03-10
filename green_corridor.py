import json
import random
import time

while True:

    with open("traffic_state.json") as f:
        data=json.load(f)

    area=random.choice(["Area A","Area B","Area C"])

    lane=random.choice(["Lane 1","Lane 2","Lane 3","Lane 4"])

    path=[

        f"{area} Signal 1",
        f"{area} Signal 2",
        f"{area} Signal 3"

    ]

    data["ambulance"]={

        "area":area,
        "lane":lane,
        "green_corridor":path

    }

    with open("traffic_state.json","w") as f:
        json.dump(data,f,indent=2)

    print("Ambulance detected")

    time.sleep(10)
