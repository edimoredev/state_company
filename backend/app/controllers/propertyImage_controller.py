from fastapi import HTTPException, status
from app.adapters.database.dbmongo import conn
import pymongo


class PropertyImageController():
    """
    Class that manages operations related to propertyImage in the database.
    """
    def create_propertyImage(self, id_property_image):
        """
        Creates a new propertyImage in the database.
        :param id_property_image: A dictionary representing the propertyImage to be created.
        """
        try:
            conn.property_image.insert_one(id_property_image)
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")

    def get_all_propertyImage(self):
        """
        Retrieves a list of all propertyImage from the database.
        :return: A list of propertyImage dictionaries.
        """
        try:
            propertyImage = conn.property_image.find().sort("id_property_image", pymongo.ASCENDING)
            return list(propertyImage)
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")
        
    def search_propertyImage_by_id(self, id_property_image: int) -> dict:
        """
        Searches for an propertyImage in the database by their ID.
        :param id_property_image: The ID of the propertyImage to search for.
        :return: The propertyImage dictionary if found, or None.
        """
        try:
            propertyImage = conn.property_image.find({'id_property_image': id_property_image})
            return propertyImage
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")