from typing import List

def propertyTrace_schema(propertyTrace)-> dict:
    return {
        "id_property_trace" : propertyTrace["id_property_trace"],
        "date_sale" : propertyTrace["date_sale"],
        "name" : propertyTrace["name"],
        "value" : propertyTrace["value"],
        "tax" : propertyTrace["tax"],
        "id_property" : propertyTrace["id_property"]
    }

def propertiesTrace_schema(propertiesTrace: List[dict])-> List[dict]:
    return [propertyTrace_schema(propertyTrace) for propertyTrace in propertiesTrace]