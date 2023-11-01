from pydantic import BaseModel

class Property(BaseModel):
    id_property: int
    name: str
    address:str
    price:float
    code_internal:str
    year:int
    id_owner:int