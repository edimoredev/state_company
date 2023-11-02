from fastapi import HTTPException, status
from app.adapters.database.dbmongo import conn
import pymongo

class PropertyTraceController():
    """
    Class that manages operations related to propertyTrace in the database.
    """
    def create_propertyTrace(self, id_property_trace):
        """
        Creates a new propertyTrace in the database.
        :param id_property_trace: A dictionary representing the propertyTrace to be created.
        """
        try:
            conn.property_trace.insert_one(id_property_trace)
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")
        
    def get_all_propertyTrace(self):
        """
        Retrieves a list of all propertyTrace from the database.
        :return: A list of propertyTrace dictionaries.
        """
        try:
            propertyTrace = conn.property_trace.find().sort("id_property_trace", pymongo.ASCENDING)
            return list(propertyTrace)
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")
        
    def search_propertyTrace_by_id(self, id_property_trace: int) -> dict:
        """
        Searches for an propertyTrace in the database by their ID.
        :param id_property_trace: The ID of the propertyTrace to search for.
        :return: The propertyTrace dictionary if found, or None.
        """
        try:
            propertyTrace = conn.property_trace.find({'id_property_trace': id_property_trace})
            return propertyTrace
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")