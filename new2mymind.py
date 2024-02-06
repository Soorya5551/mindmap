import json

def build_tree(data, parent_id='nan'):
  
    children = [node for node in data if node['parent'] == parent_id]

   
    nodes = []
    for child in children:
        child_id = child['child']
        idd=child['parent'],
        texts= child['description']
        child_node = {
            'id': child_id,
            'text': child['description'],
            'children': build_tree(data, parent_id=texts)
        }
        nodes.append(child_node)

    return nodes

def convert_json_to_tree(json_data):
    data = json_data['nodes']


    root_nodes = [node for node in data if node['parent'] == 'nan']


    tree = []

  
    for root_node in root_nodes:
        root_id = root_node['child']
        idddd=root_node['parent']
        text= root_node['description']
        root = {
            'id': root_id,
            'text': root_node['description'],
            'children': build_tree(data, parent_id=text)
        }
        tree.append(root)

    return tree

if __name__ == "__main__":
   
    
    with open('objectives_hierarchy.json', 'r') as f:
        json_data = json.load(f)
    mindmap_dict = {
        "root": {
            "id": "mihylbmz",
            "text": "My Mind Map",
            "notes": "",
            "layout": "map",
            "children": []
        }
    }
    nested_tree = convert_json_to_tree(json_data)


    mindmap_dict["root"]["children"] = nested_tree

    result_json = json.dumps(mindmap_dict, indent=2)

    with open("m4.mymind", "w") as mymind_file:
       mymind_file.write(result_json)
print("Mind map creation complete. Output saved to 'm4.mymind'.")