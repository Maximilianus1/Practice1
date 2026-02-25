import json
file= open('./sample-data.json', "r")
json_data =json.load(file)
print("Interface Status")
print("================================================================================")
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-------------------------------------------------- --------------------  ------  ------")
for item in json_data["imdata"]:
    dn=item["l1PhysIf"]["attributes"]["dn"]
    descr = item["l1PhysIf"]["attributes"]["descr"]
    speed = item["l1PhysIf"]["attributes"]["speed"]
    mtu=item["l1PhysIf"]["attributes"]["mtu"]
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")