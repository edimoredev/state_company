from fastapi import APIRouter, HTTPException, status
from app.schemas.propertyImage_schema import propertiesImage_schema
#>>> Import controllers
from app.controllers.propertyImage_controller import PropertyImageController
#>>> Import models
from app.models.propertyImage_model import PropertyImageModel

# Create a router to handle operations related to propertyImage
propertyImageRouter = APIRouter(prefix="/propertyImage",
                       tags=["PropertyImage"],
                       responses={status.HTTP_404_NOT_FOUND: {"message": "Not Found"}})

@propertyImageRouter.post('/',response_model= PropertyImageModel, status_code = status.HTTP_201_CREATED)
async def create_propertyImage(propertyImage: PropertyImageModel):
    """
    Create a new propertyImage in the database.
    :param propertyImage: Data of the propertyImage to create.
    """
    # Check if the propertyImage already exists
    existing_propertyImage = propertiesImage_schema(PropertyImageController().search_propertyImage_by_id(propertyImage.id_property_image))
    # Valid existing_propertyImage
    if existing_propertyImage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="PropertyImage already exists"
        )
    # Convert to a dictionary
    propertyImage_dict = dict(propertyImage)
    # Create the propertyImage using the controller
    PropertyImageController().create_propertyImage(propertyImage_dict)
    return propertyImage

# Define a route to get all propertiesImage
@propertyImageRouter.get('/',response_model= list[PropertyImageModel])
async def get_all_propertyImage():
    """
    Get a list of all propertiesImage in the database.
    """
    propertiesImage = propertiesImage_schema(PropertyImageController().get_all_propertyImage())
    return propertiesImage

# Define a route to get an propertyImage by their ID
@propertyImageRouter.get('/{id_property_image}')
async def get_property(id_property_image: int):
    """
    Get an propertyImage by their ID.

    :param id_property_image: ID of the propertyImage to search for.
    """
    # Search for an propertyImage by their ID using the controller
    propertyImage = propertiesImage_schema(PropertyImageController().search_propertyImage_by_id(id_property_image))
    # Valid propertyImage and retur message
    if not propertyImage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="PropertyImage not found"
        )
    return propertyImage