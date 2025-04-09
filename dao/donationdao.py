import mysql.connector
from exceptions.InsufficientFundsException import InsufficientFundsException
from exceptions.AdoptionException import AdoptionException

class DonationDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def add_cash_donation(self, donation):
        try:
            query = "INSERT INTO cash_donations (donor, amount, donation_date) VALUES (%s, %s, %s)"
            values = (donation.get_donor(), donation.get_amount(), donation.get_donation_date())
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Cash donation recorded successfully.")
        except mysql.connector.Error as e:
            raise AdoptionException(f"Failed to record donation: {str(e)}")


    def add_item_donation(self, donor_name, amount, item_type):
        query = "insert into cash_donations (donor, amount, item_type) values (%s, %s, %s)"
        self.cursor.execute(query, (donor_name, amount, item_type))
        self.conn.commit()

    def list_all_donations(self):
        query = """SELECT donor, amount AS value, donation_date FROM cash_donations
            UNION
            SELECT donor_name, NULL AS value, donation_date FROM item_donation;
            """
        self.cursor.execute(query)
        return self.cursor.fetchall()
