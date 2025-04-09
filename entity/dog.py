class dog:
    def __init__(self, name, age, breed, dog_breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.dog_breed = dog_breed
        self.pet_type = 'dog'

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_breed(self):
        return self.breed

    def get_dog_breed(self):
        return self.dog_breed

    def get_cat_color(self):
        return None

    def get_type(self):
        return self.pet_type
