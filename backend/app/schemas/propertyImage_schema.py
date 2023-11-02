from typing import List

def propertyImage_schema(propertyImage)-> dict:
    return {
        "id_property_image" : propertyImage["id_property_image"],
        "file" : propertyImage["file"],
        "enable" : propertyImage["enable"],
        "id_property" : propertyImage["id_property"]
    }

def propertiesImage_schema(propertiesImage: List[dict])-> List[dict]:
    return [propertyImage_schema(propertyImage) for propertyImage in propertiesImage]