from dao.petdao import PetDAO
from dao.petshelterdao import PetShelterDAO
from dao.donationdao import DonationDAO
from dao.adoptioneventdao import AdoptionEventDAO
from exceptions.InvalidPetAgeException import InvalidPetAgeException
from exceptions.NullReferenceException import NullReferenceException
from exceptions.InsufficientFundsException import InsufficientFundsException
from exceptions.FileHandlingException import FileHandlingException
from exceptions.AdoptionException import AdoptionException
from entity.dog import dog
from entity.cat import cat
from entity.cashdonation import cashdonation
from util.config import connect_db
from datetime import datetime

if __name__ == "__main__":
    connection = connect_db()
    pet_dao = PetDAO(connection)
    shelter_dao = PetShelterDAO(connection)
    donation_dao = DonationDAO(connection)
    adoption_event_dao = AdoptionEventDAO(connection)

    while True:
        print("\n=== PetPals Main Menu ===")
        print("1. Add a Pet")
        print("2. List All Pets")
        print("3. Make Cash Donation")
        print("4. Host Adoption Event")
        print("5. List All Shelters")
        print("6. Register Pet to Shelter")
        print("7. View All Donations")
        print("8. Register Participant to Event")
        print("9. List All Adoption Events")
        print("10. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter pet name: ")
                age = int(input("Enter pet age: "))
                if age <= 0:
                    raise InvalidPetAgeException("Pet age must be a positive integer.")
                breed = input("Enter breed: ")
                pet_type = input("Enter type (dog/cat): ").lower()
                if pet_type == "dog":
                    dog_breed = input("Enter specific dog breed: ")
                    pet = dog(name, age, breed, dog_breed)
                elif pet_type == "cat":
                    cat_color = input("Enter cat color: ")
                    pet = cat(name, age, breed, cat_color)
                pet_dao.add_pet(pet)
                print("Pet added successfully.")

            elif choice == "2":
                print("\nAll Pets:")
                pets = pet_dao.list_all_pets()
                for pet in pets:
                    try:
                        if pet[1] is None or pet[2] is None:
                            raise NullReferenceException("Pet has missing attributes.")
                        print(pet)
                    except NullReferenceException as e:
                        print(e)

            elif choice == "3":
                donor = input("Enter donor name: ")
                amount = float(input("Enter donation amount: "))
                if amount < 10:
                    raise InsufficientFundsException("Minimum donation amount is $10.")
                donation = cashdonation(donor, amount, datetime.now())
                donation_dao.add_cash_donation(donation)

            elif choice == "4":
                available_pets = pet_dao.list_all_pets()
                if not available_pets:
                    raise AdoptionException("No pets available for adoption.")
                event_name = input("Enter the name of the adoption event: ")
                adoption_event_dao.host_event(event_name)
                print("Adoption event hosted successfully.")

            elif choice == "5":
                print("All Pet Shelters:")
                shelters = shelter_dao.list_all_shelters()
                for s in shelters:
                    print(s)

            elif choice == "6":
                pet_id = int(input("Enter Pet ID: "))
                shelter_id = int(input("Enter Shelter ID: "))
                shelter_dao.register_pet_to_shelter(pet_id, shelter_id)

            elif choice == "7":
                print("All Donations:")
                donations = donation_dao.list_all_donations()
                for d in donations:
                    print(d)

            elif choice == "8":
                event_id = int(input("Enter Event ID: "))
                participant_id = int(input("Enter Participant ID: "))
                participant_type = input("Enter Participant Type (pet/human): ")
                adoption_event_dao.register_participant(event_id, participant_id, participant_type)

            elif choice == "9":
                print("All Adoption Events:")
                events = adoption_event_dao.list_events()
                for e in events:
                    print(e)

            elif choice == "10":
                print("Exiting the application.")
                break

            else:
                print("Invalid choice. Please try again.")

        except (InvalidPetAgeException, NullReferenceException, InsufficientFundsException,
                FileHandlingException, AdoptionException, ValueError) as e:
            print(f"Error: {e}")
