from pydantic import BaseModel

class PropertyImageModel(BaseModel):
    """
    Class representing an propertyImageModel.
    """
    id_property_image: int
    file: str
    enable: bool
    id_property: int