from fastapi import HTTPException, status
from adapters.database.dbmongo import conn
import pymongo


class OwnerController():
    """
    Class that manages operations related to owners in the database.
    """

    def create_owner(self, owner: dict):
        """
        Creates a new owner in the database.
        :param owner: A dictionary representing the owner to be created.
        """
        try:
            conn.owner.insert_one(owner)
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")

    def get_all_owner(self) -> list:
        """
        Retrieves a list of all owners from the database.
        :return: A list of owner dictionaries.
        """
        try:
            owners = conn.owner.find().sort("id_owner", pymongo.ASCENDING)
            return list(owners)
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")

    def search_owner_by_id(self, id_owner: int) -> dict:
        """
        Searches for an owner in the database by their ID.
        :param id_owner: The ID of the owner to search for.
        :return: The owner dictionary if found, or None.
        """
        try:
            owner = conn.owner.find({'id_owner': id_owner})
            return owner
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Database connection not found")