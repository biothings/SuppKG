import json

f = open('supp_kg.json')

original_data = json.load(f)

links = original_data["links"]
nodes = original_data["nodes"]


#finds index of node corresponding to original source and target
def get_nodes_index(val):
    for i in nodes:
        if i["id"] == val:
            return nodes.index(i)


parsed_data = {"relations": []}

for i in range(len(links)):
    source_key = get_nodes_index(links[i]["source"])
    target_key = get_nodes_index(links[i]["target"])
    
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
    entries["predicate"] = links[i]["key"]

    parsed_data["relations"].append(entries)

#write parsed data to data.json 
with open('data.json', 'w') as f:
    json.dump(parsed_data, f)
