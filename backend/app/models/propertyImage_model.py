from pydantic import BaseModel
from typing import Optional

class PropertyImageModel(BaseModel):
    """
    Class representing an propertyImageModel.
    """
    id_property_image: int
    enable: bool
    id_property: int

class propertyImageOut(PropertyImageModel):
    file_name: Optional[str]