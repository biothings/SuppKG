import json

f = open('supp_kg.json')

original_data = json.load(f)

links = original_data["links"]
nodes = original_data["nodes"]

# dictionary with node id and corresponding index
nodes_ids = {}

for node in nodes:
    nodes_ids[node['id']] = nodes.index(node)


# finds index of node corresponding to original source and target
def get_nodes_index(val):
    return nodes_ids[val]


parsed_data = {"relations": []}

# reformat link objects
for link in links:
    source_key = get_nodes_index(link["source"])
    target_key = get_nodes_index(link["target"])

    entries = {}
    entries["_id"] = link["source"]+"_" + \
        link["target"]+"_"+link["key"]
    entries["subject"] = {"umls": link["source"],
                          "name": nodes[source_key]["terms"][0],
                          "semtypes": nodes[source_key]["semtypes"]}
    entries["relation"] = link["relations"]
    entries["object"] = {"umls": link["target"],
                         "name": nodes[target_key]["terms"][0],
                         "semtypes": nodes[target_key]["semtypes"]}
    entries["predicate"] = link["key"]

    parsed_data["relations"].append(entries)

# write parsed data to data.json
with open('data.json', 'w') as f:
    json.dump(parsed_data, f)
