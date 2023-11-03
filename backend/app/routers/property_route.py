from fastapi import APIRouter, HTTPException, status
from app.schemas.property_schema import  properties_schema
from app.schemas.owner_schema import owners_schema
#>>> Import controllers
from app.controllers.property_controller import PropertyController
from app.controllers.owner_controller import OwnerController
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
    # Check if the property already exists
    existing_property = properties_schema(PropertyController().search_property_by_id(property.id_property))
    # Valid existing_property
    if existing_property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property already exists"
        )
    # Check if the owner already exists
    existing_owner = owners_schema(OwnerController().search_owner_by_id(property.id_owner))
    if not existing_owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner does not already exists"
        )
    # Convert to a dictionary
    property_dict = dict(property)
    # Create the property using the controller
    PropertyController().create_property(property_dict)
    return property

@propertyRouter.put('/', response_model= PropertyModel, status_code = status.HTTP_200_OK)
async def put_price_property(property: PropertyModel):
    """
    Update price property in the database.
    :param property: Data of the property to update.
    """
    # Check if the property already exists
    existing_property = properties_schema(PropertyController().search_property_by_id(property.id_property))
    if not existing_property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property does not exists"
        )
    # update the price property using the controller
    PropertyController().update_price(property.id_property, property.price)
    return property
    
# Define a route to get all properties
@propertyRouter.get('/',response_model= list[PropertyModel])
async def get_all_property():
    """
    Get a list of all properties in the database.
    """
    properties = properties_schema(PropertyController().get_all_property())
    return properties

# Define a route to get an property by their ID
@propertyRouter.get('/{id_property}')
async def get_property(id_property: int):
    """
    Get an property by their ID.

    :param id_property: ID of the property to search for.
    """
    # Search for an property by their ID using the controller
    property = properties_schema(PropertyController().search_property_by_id(id_property))
    # Valid property and retur message
    if not property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found"
        )
    return property
    
  