from typing import List

def property_schema(property)-> dict:
    return {
        "id_property" : property["id_property"],
        "name" : property["name"],
        "address" : property["address"],
        "price" : property["price"],
        "code_internal":property["code_internal"],
        "year" : property["year"],
        "id_owner": property["id_owner"]
    }

def properties_schema(properties: List[dict])-> List[dict]:
    return [property_schema(property) for property in properties]
