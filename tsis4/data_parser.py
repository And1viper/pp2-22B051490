import json
import random #to make examples

with open("sample-data.json", "r") as sample_data:
    data = json.load(sample_data)

num = int(input("How many lines to print?\n"))

print("Interface Status\n================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
while num > 0:
    item = random.choice(data["imdata"])
    item_attr = item["l1PhysIf"]["attributes"]
    print("{:<51} {:<19} {:<9} {:<6}".format(item_attr["dn"], item_attr["descr"], item_attr["speed"], item_attr["mtu"]))
    num -= 1