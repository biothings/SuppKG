import json
import os


# create dictionary with nodes id as key and index as value
def create_id_index_map(nodes: list) -> dict:
    id_index_map = {}
    for index, node in enumerate(nodes):
        id_index_map[node['id']] = index
    return id_index_map


# create document id from a link object
def create_doc_id(link: dict) -> str:
    return link["source"] + "_" + link["target"] + "_" + link["key"]


def load_data(data_folder):
    # load original data
    with open(os.path.join(data_folder, 'supp_kg.json')) as f:
        original_data = json.load(f)

    links = original_data["links"]
    nodes = original_data["nodes"]

    node_id_index_map = create_id_index_map(nodes)

    for link in links:
        source_index = node_id_index_map[link["source"]]
        target_index = node_id_index_map[link["target"]]
        source_node = nodes[source_index]
        target_node = nodes[target_index]

        doc = {}
        doc["_id"] = create_doc_id(link)
        doc["subject"] = {
            "umls": link["source"],
            "name": source_node["terms"][0],
            "semtypes": source_node["semtypes"]
        }
        doc["object"] = {
            "umls": link["target"],
            "name": target_node["terms"][0],
            "semtypes": target_node["semtypes"]
        }
        doc["relation"] = link["relations"]
        doc["predicate"] = link["key"]

        yield doc
