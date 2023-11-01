from fastapi import APIRouter, HTTPException, status
from app.schemas.property_schema import  properties_schema
#>>> controllers
from app.controllers.property_controller import PropertyController
#>>> models
from app.models.property_model import Property


# add route propertyRouter, prefix, tags and response
propertyRouter = APIRouter(prefix="/property",
                       tags=["Property"],
                       responses={status.HTTP_404_NOT_FOUND: {"message": "Not Found"}})


@propertyRouter.get('/',response_model= list[Property])
async def get_all_property():
    properties = properties_schema(PropertyController().get_all_property())
    return properties

@propertyRouter.post('/', response_model= Property, status_code = status.HTTP_201_CREATED)
async def create_property(property: Property):
    propert_dict = dict(property)
    PropertyController().create_property(propert_dict)
    return property
    
  