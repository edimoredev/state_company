from pydantic import BaseModel

class PropertyTraceModel(BaseModel):
    """
    Class representing an propertyTrace.
    """
    id_property_trace: int
    date_sale: str
    name: str
    value: float
    tax: float
    id_property: int
