import pandas as pd
import json

def generate_objectives_hierarchy(csv_file_path, output_json_path):

    df = pd.read_csv(csv_file_path)

    hierarchy_dict = {"nodes": []}

    for index, row in df.iterrows():

        obj_id = str(row["Obj Id"])
        parent_obj = str(row["Parent Objective"])
        objective = str(row["Objective"])

        objective_dict = {
            "parent": parent_obj,
            "child": obj_id,
            "description": objective
        }

        hierarchy_dict["nodes"].append(objective_dict)

    json_output = json.dumps(hierarchy_dict, indent=2)

    with open(output_json_path, "w") as json_file:
        json_file.write(json_output)

    print(f"Conversion complete. Output saved to '{output_json_path}'.")

csv_file_path = r"C:\xampp\htdocs\internship\mindmap\obj_data.csv"
output_json_path = r"C:\xampp\htdocs\internship\mindmap\objectives_hierarchy.json"

generate_objectives_hierarchy(csv_file_path, output_json_path)
