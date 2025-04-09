import mysql.connector
from exceptions.AdoptionException import AdoptionException

class PetShelterDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def register_pet_to_shelter(self, pet_id, shelter_id):
        try:
            query = "UPDATE pet_shelter SET pet_id = %s WHERE shelter_id = %s"
            self.cursor.execute(query, (pet_id, shelter_id))
            self.conn.commit()
            print("Pet registered to shelter successfully.")
        except mysql.connector.Error as e:
            raise AdoptionException(f"Failed to register pet to shelter: {str(e)}")

    def remove_pet_from_shelter(self, shelter_id):
        try:
            query = "UPDATE pet_shelter SET pet_id = NULL WHERE shelter_id = %s"
            self.cursor.execute(query, (shelter_id,))
            self.conn.commit()
        except mysql.connector.Error as e:
            raise AdoptionException(f"Failed to remove pet from shelter: {str(e)}")

    def list_all_shelters(self):
        try:
            query = "SELECT * FROM pet_shelter"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving shelters: {e}")
            return []
