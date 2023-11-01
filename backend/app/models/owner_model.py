from pydantic import BaseModel

class Owner(BaseModel):
    id_owner: int
    name: str
    address:str
    photo:str
    birhday: str