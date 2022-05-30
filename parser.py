import json


def load_data(data_folder):
    # load original data
    with open(data_folder + '/' + 'supp_kg.json') as f:
        original_data = json.load(f)

    links = original_data["links"]
    nodes = original_data["nodes"]

    # create dictionary with nodes id as key and index as value
    nodes_ids = {}

    for node in nodes:
        nodes_ids[node['id']] = nodes.index(node)

    # looks index of node corresponding to original source and target
    def get_nodes_index(val):
        return nodes_ids[val]

    for link in links:
        source_key = get_nodes_index(link["source"])
        target_key = get_nodes_index(link["target"])

        parsed_data = {}
        parsed_data["_id"] = link["source"]+"_" + \
            link["target"]+"_"+link["key"]
        parsed_data["subject"] = {"umls": link["source"],
                                  "name": nodes[source_key]["terms"][0],
                                  "semtypes": nodes[source_key]["semtypes"]}
        parsed_data["relation"] = link["relations"]
        parsed_data["object"] = {"umls": link["target"],
                                 "name": nodes[target_key]["terms"][0],
                                 "semtypes": nodes[target_key]["semtypes"]}
        parsed_data["predicate"] = link["key"]

        yield parsed_data
