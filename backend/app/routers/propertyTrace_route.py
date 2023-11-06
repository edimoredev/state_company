from fastapi import APIRouter, HTTPException, status
from schemas.propertyTrace_schema import propertiesTrace_schema
from schemas.property_schema import properties_schema
#>>> Import controllers
from controllers.propertyTrace_controller import PropertyTraceController
from controllers.property_controller import PropertyController
#>>> Import models
from models.propertyTrace_model import PropertyTraceModel

# Create a router to handle operations related to propertyTrace
propertyTraceRouter = APIRouter(prefix="/propertyTrace",
                       tags=["PropertyTrace"],
                       responses={status.HTTP_404_NOT_FOUND: {"message": "Not Found"}})

@propertyTraceRouter.post('/',response_model= PropertyTraceModel, status_code = status.HTTP_201_CREATED)
async def create_propertyTrace(propertyTrace: PropertyTraceModel):
    """
    Create a new propertyTrace in the database.
    :param propertyTrace: Data of the propertyTrace to create.
    """
    # Check if the propertyTrace already exists
    existing_propertyTrace = propertiesTrace_schema(PropertyTraceController().search_propertyTrace_by_id(propertyTrace.id_property_trace))
    # Valid existing_propertyTrace
    if existing_propertyTrace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="PropertyImage already exists"
        )
    
    # Check if the property not already exists
    existing_property = properties_schema(PropertyController().search_property_by_id(propertyImage.id_property))
    if not existing_property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property does not exists"
        )
    # Convert to a dictionary
    propertyTrace_dict = dict(propertyTrace)
    # Create the propertyTrace using the controller
    PropertyTraceController().create_propertyTrace(propertyTrace_dict)
    return propertyTrace

# Define a route to get all propertiesTrace
@propertyTraceRouter.get('/',response_model= list[PropertyTraceModel])
async def get_all_propertyTrace():
    """
    Get a list of all propertiesTrace in the database.
    """
    propertiesTrace = propertiesTrace_schema(PropertyTraceController().get_all_propertyTrace())
    return propertiesTrace

# Define a route to get an propertyTrace by their ID
@propertyTraceRouter.get('/{id_property_trace}')
async def get_property(id_property_trace: int):
    """
    Get an propertyTrace by their ID.

    :param id_property_trace: ID of the propertyTrace to search for.
    """
    # Search for an propertyImage by their ID using the controller
    propertyTrace = propertiesTrace_schema(PropertyTraceController().search_propertyTrace_by_id(id_property_trace))
    # Valid propertyTrace and retur message
    if not propertyTrace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="PropertyTrace not found"
        )
    return propertyTrace