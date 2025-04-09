import mysql.connector
from exceptions.AdoptionException import AdoptionException
from datetime import datetime

from util.config import connect_db

class AdoptionEventDAO:
    def __init__(self, connection):
        try:
            self.conn = connection
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            raise AdoptionException(f"Database connection failed: {str(e)}")

    def host_event(self, event_name):
        try:
            event_date = datetime.now()
            query = "INSERT INTO adoption_events (event_name, event_date) VALUES (%s, %s)"
            self.cursor.execute(query, (event_name, event_date))
            self.conn.commit()
        except mysql.connector.Error as e:
            raise AdoptionException(f"Failed to host adoption event: {str(e)}")

    def register_participant(self, event_id, participant_id, participant_type):
        try:
            query = "INSERT INTO event_participants (event_id, participant_id, participant_type) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (event_id, participant_id, participant_type))
            self.conn.commit()
            print("Participant registered successfully.")
        except mysql.connector.Error as e:
            raise AdoptionException(f"Failed to register participant: {str(e)}")

    def list_events(self):
        try:
            query = "SELECT * FROM adoption_events"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            raise AdoptionException(f"Failed to retrieve events: {str(e)}")
