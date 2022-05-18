import json

f = open('supp_kg.json')

data = json.load(f)

links = data["links"]
nodes = data["nodes"]


def get_nodes_key(val):
    for i in nodes:
        if i["id"] == val:
            return nodes.index(i)


print(get_nodes_key('C0151763'))
print(nodes[get_nodes_key('DC1029148')])

json = []

for i in range(3):
    source_key = get_nodes_key(links[i]["source"])
    target_key = get_nodes_key(links[i]["target"])
    entries = {}
    entries["_id"] = links[i]["source"]+"_" + \
        links[i]["target"]+"_"+links[i]["key"]
    entries["subject"] = {"umls": links[i]["source"],
                          "name": nodes[source_key]["terms"][0],
                          "semtypes": nodes[source_key]["semtypes"]}
    entries["relation"] = links[i]["relations"]
    entries["object"] = {"umls": links[i]["target"],
                         "name": nodes[target_key]["terms"][0],
                         "semtypes": nodes[target_key]["semtypes"]}

    json.append(entries)

print(json)
