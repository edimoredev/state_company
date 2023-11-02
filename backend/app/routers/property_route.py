from fastapi import APIRouter, HTTPException, status
from app.schemas.property_schema import  properties_schema
#>>> Import controllers
from app.controllers.property_controller import PropertyController
#>>> Import models
from app.models.property_model import PropertyModel


# Create a router to handle operations related to property
propertyRouter = APIRouter(prefix="/property",
                       tags=["Property"],
                       responses={status.HTTP_404_NOT_FOUND: {"message": "Not Found"}})

@propertyRouter.post('/', response_model= PropertyModel, status_code = status.HTTP_201_CREATED)
async def create_property(property: PropertyModel):
    """
    Create a new property in the database.
    :param property: Data of the property to create.
    """
    # Check if the owner already exists
    existing_property = properties_schema(PropertyController().search_property_by_id(property.id_property))
    # Valid existing_owner
    if existing_property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner already exists"
        )
    # Convert to a dictionary
    propert_dict = dict(property)
    # Create the property using the controller
    PropertyController().create_property(propert_dict)
    return property

# Define a route to get all properties
@propertyRouter.get('/',response_model= list[PropertyModel])
async def get_all_property():
    """
    Get a list of all properties in the database.
    """
    properties = properties_schema(PropertyController().get_all_property())
    return properties

# Define a route to get an owner by their ID
@propertyRouter.get('/{id_property}')
async def get_owner(id_property: int):
    """
    Get an owner by their ID.

    :param id_owner: ID of the owner to search for.
    """
    # Search for an owner by their ID using the controller
    owner = properties_schema(PropertyController().search_property_by_id(id_property))
    # Valid owner and retur message
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found"
        )
    return owner
    
  