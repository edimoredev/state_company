from app.adapters.database.dbmongo import conn


class PropertyController():

    def get_all_property(self):
        users = conn.property.find()
        return list(users)
    
    def create_property(self, property):
        conn.property.insert_one(property)