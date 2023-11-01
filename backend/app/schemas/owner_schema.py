from typing import List

def owner_schema(owner: dict) -> dict:
    """
    Transform a dictionary representing an owner into a structured dictionary.
    """
    return {
        "id_owner": owner["id_owner"],
        "name": owner["name"],
        "address": owner["address"],
        "photo": owner["photo"],
        "birthday": owner["birthday"]
    }

def owners_schema(owners: List[dict]) -> List[dict]:
    """
    Transform a list of owner dictionaries into a list of structured dictionaries.
    """
    return [owner_schema(owner) for owner in owners]
