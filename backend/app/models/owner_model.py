from pydantic import BaseModel

class OwnerModel(BaseModel):
    """
    Class representing an owner.
    """
    id_owner: int
    name: str
    address: str
    photo: str
    birthday: str