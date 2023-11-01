from app.adapters.database.dbmongo import conn


class PropertyController():

    def get_all_property(self):
        property = conn.property.find()
        return list(property)
    
    def create_property(self, property):
        conn.property.insert_one(property)