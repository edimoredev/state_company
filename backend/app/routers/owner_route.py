from fastapi import APIRouter, HTTPException, status
from app.schemas.owner_schema import owners_schema
#>>> Import controllers
from app.controllers.owner_controller import OwnerController
#>>> Import models
from app.models.owner_model import OwnerModel

# Create a router to handle operations related to owners
ownerRouter = APIRouter(
    prefix="/owner",  # Route prefix
    tags=["Owner"],   # Tag to group routes in documentation
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not Found"}}  # Default response for 404 errors
)

# Define a route to create an owner
@ownerRouter.post('/', response_model=OwnerModel, status_code=status.HTTP_201_CREATED)
async def create_owner(owner: OwnerModel):
    # Check if the owner already exists
    existing_owner = owners_schema(OwnerController().search_owner_by_id_owner(owner.id_owner))
     # Valid existing_owner
    if existing_owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner already exists"
        )
    # Transform to dic
    owner_dict = dict(owner)
    # Create the owner using the controller
    OwnerController().create_owner(owner_dict)
    return owner

# Define a route to get all owners
@ownerRouter.get('/', response_model=list[OwnerModel])
async def get_all_owner():
    # Get all owners using the controller
    owners = owners_schema(OwnerController().get_all_owner())
    # Valid owners and retur message
    if not owners:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owners not found"
        )
    return owners

# Define a route to get an owner by their ID
@ownerRouter.get('/{owner}')
async def get_owner(owner: int):
    # Search for an owner by their ID using the controller
    owner = owners_schema(OwnerController().search_owner_by_id_owner(owner))
    # Valid owner and retur message
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found"
        )
    return owner


