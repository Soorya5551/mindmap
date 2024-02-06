import json

# Your JSON data as a string
json_data = '''
{
  "nodes": [
    {
      "parent": "Incorporating LLC in US For the product parent",
      "child": "67a3cf5e",
      "description": "Applying For Us B1 visa To be ready for travel anytime"
    },
    {
      "parent": "T - Add more security for the product",
      "child": "9af5dc8e",
      "description": "T - Testing the build regularly to ensure security"
    },

    {
      "parent": "T - Add more security for the product",
      "child": "af6ebdca",
      "description": "T - Creating new test cases to ensure security"
    },
    {
      "parent": "nan",
      "child": "8a730e7b",
      "description": "T - Add more security for the product"
    },
    {
      "parent": "Improving OKR So as to make it to the ZERO process usable state!",
      "child": "367d17fe",
      "description": "Change The OKR logo To make it appealing"
    },
    {
      "parent": "nan",
      "child": "daa6e476",
      "description": "Improving OKR So as to make it to the ZERO process usable state!"
    },
    {
      "parent": "Building Leika To disrupt the data insights in pharmacy RWE R&D and Commercial domain",
      "child": "6c341136",
      "description": "Featuring [Must] Capability to export to put data for presentation, action invoker etc..."
    },
    {
      "parent": "T - Testing the build regularly to ensure security",
      "child": "87b64c6c",
      "description": "T - Setting up Test environment to test"
    },
    {
      "parent": "Incorporating LLC in US For the product parent",
      "child": "e982fce5",
      "description": "Monetize/maximize brand reach Using data and other pillars [ Commercialization, Productization, Operations / all administrative works ] To monetize"
    },
    {
      "parent": "Featuring Bio update and badge To show the maturity and data update correctness",
      "child": "d001a307",
      "description": "Receiving Storylinedemo from Nakul To build the feature"
    },
    {
      "parent": "Building Leika To disrupt the data insights in pharmacy RWE R&D and Commercial domain",
      "child": "acbed3ed",
      "description": "Featuring Bio update and badge To show the maturity and data update correctness"
    },
    {
      "parent": "Incorporating LLC in US For the product parent",
      "child": "1ab45",
      "description": "Building Leika To disrupt the data insights in pharmacy RWE R&D and Commercial domain"
    },
    {
      "parent": "Incorporating LLC in US For the product parent",
      "child": "2ab45",
      "description": "Building The website For the Incorporation and the product details"
    },
    {
      "parent": "Incorporating LLC in US For the product parent",
      "child": "3ab45",
      "description": "Reservation Of the Domain For website"
    },
    {
      "parent": "nan",
      "child": "4ab45",
      "description": "Incorporating LLC in US For the product parent"
    },
    {
      "parent": "Building Leika To disrupt the data insights in pharmacy RWE R&D and Commercial domain",
      "child": "5ab45",
      "description": "Featuring  [Could] Data insights that can be a content or case study for ivyleague health are MBA or any relevant courses"
    },
    {
      "parent": "T - Setting up Test environment to test",
      "child": "b470ae09",
      "description": "T - Testing automatically in order to save time"
    }
  ]
}
'''

try:
    # Load JSON data
    data = json.loads(json_data)

    # If you want to check for the presence of the "nodes" key
    if 'nodes' in data:
        print("JSON format is correct.")
    else:
        print("JSON format is incorrect. Missing 'nodes' key.")

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
