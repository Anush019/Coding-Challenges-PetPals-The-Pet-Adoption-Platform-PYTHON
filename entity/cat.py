class cat:
    def __init__(self, name, age, breed, cat_color):
        self.name = name
        self.age = age
        self.breed = breed
        self.cat_color = cat_color
        self.pet_type = 'cat'

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_breed(self):
        return self.breed

    def get_cat_color(self):
        return self.cat_color

    def get_dog_breed(self):
        return None

    def get_type(self):
        return self.pet_type
