from fastapi import HTTPException, status
from adapters.database.dbmongo import conn
import pymongo


class PropertyController():
    """
    Class that manages operations related to property in the database.
    """
    def create_property(self, property: dict):
        """
        Creates a new property in the database.
        :param property: A dictionary representing the property to be created.
        """
        try:
            conn.property.insert_one(property)
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")

    def update_price(self, id_property: int, new_price: float):
        """
        update the price for property in the database.
        :param price: A dictionary representing the property to be update.
        :return: A list of property update dictionaries.
        """
        try:
            # Define el filtro para encontrar la propiedad por su ID
            filter = {"id_property": id_property}
            # Define las modificaciones para actualizar el precio
            update = {"$set": {"price": new_price}}
            # Crea una actualización con los campos y valores que deseas cambiar
            conn.property.update_one(filter, update)
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")


    def get_all_property(self):
        """
        Retrieves a list of all property from the database.
        :return: A list of property dictionaries.
        """
        try:
            property = conn.property.find().sort("id_property", pymongo.ASCENDING)
            return list(property)
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")
        
    def search_property_by_id(self, id_property: int) -> dict:
        """
        Searches for an property in the database by their ID.
        :param id_property: The ID of the property to search for.
        :return: The property dictionary if found, or None.
        """
        try:
            property = conn.property.find({'id_property': id_property})
            return property
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")