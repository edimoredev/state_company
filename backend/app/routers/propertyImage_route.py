from fastapi import APIRouter, HTTPException, status, UploadFile, File, Depends
import os
from schemas.propertyImage_schema import propertiesImage_schema
from schemas.property_schema import properties_schema
#>>> Import controllers
from controllers.propertyImage_controller import PropertyImageController
from controllers.property_controller import PropertyController
#>>> Import models
from models.propertyImage_model import propertyImageOut, PropertyImageModel


PATH_FILES =  os.getcwd() + "\\app\\asset\\img\\"

# Create a router to handle operations related to propertyImage
propertyImageRouter = APIRouter(prefix="/propertyImage",
                       tags=["PropertyImage"],
                       responses={status.HTTP_404_NOT_FOUND: {"message": "Not Found"}})

@propertyImageRouter.post('/', response_model= propertyImageOut,  status_code = status.HTTP_201_CREATED)
async def create_propertyImage(propertyImage:PropertyImageModel = Depends(), image: UploadFile = File(...)):
    """
    Create a new propertyImage in the database.
    :param propertyImage: Data of the propertyImage to create.
    """
    # Validar la extensión del archivo
    if not PropertyImageController().allowed_file(image.filename):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Solo se permiten archivos .png, .jpg, .jpeg")
    
    #  Check if the propertyImage already exists
    existing_propertyImage = propertiesImage_schema(PropertyImageController().search_propertyImage_by_id(propertyImage.id_property_image))
    #   Valid existing_propertyImage
    if existing_propertyImage:
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
    propertyImage_dict = dict(propertyImage)
    propertyImage_dict['file_name'] = image.filename
    print (propertyImage_dict)
    # Create the propertyImage using the controller
    PropertyImageController().create_propertyImage(propertyImage_dict)
    with open(PATH_FILES + image.filename, "wb") as img:
        img.write(image.file.read())
    return  propertyImage_dict

# Define a route to get all propertiesImage
@propertyImageRouter.get('/',response_model= list[propertyImageOut])
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