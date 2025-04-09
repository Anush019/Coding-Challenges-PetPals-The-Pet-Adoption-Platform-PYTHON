import mysql.connector
from exceptions.InvalidPetAgeException import  InvalidPetAgeException
from exceptions.NullReferenceException import  NullReferenceException
from util.config import connect_db



class PetDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def add_pet(self, pet):
        if pet.get_age() <= 0:
            raise InvalidPetAgeException("Pet age must be a positive integer.")
        query = "insert into pets (name, age, breed, type, dog_breed, cat_color) values (%s, %s, %s, %s, %s, %s)"
        values = (pet.get_name(), pet.get_age(), pet.get_breed(), pet.get_type(), pet.get_dog_breed(), pet.get_cat_color())
        self.cursor.execute(query, values)
        self.conn.commit()

    def remove_pet(self, pet_id):
        query = "delete from pets where pet_id = %s"
        self.cursor.execute(query, (pet_id,))
        self.conn.commit()

    def list_all_pets(self):
        query = "select * from pets"
        self.cursor.execute(query)
        pets = self.cursor.fetchall()
        if pets is None:
            raise NullReferenceException("No pets available.")
        return pets
