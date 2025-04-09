class AdoptionEvent:
    def __init__(self):
        self.participants = []

    def register_participant(self, participant):
        if isinstance(participant, IAdoptable):
            self.participants.append(participant)
            print("Participant registered successfully.")
        else:
            print("Error: Participant must implement IAdoptable.")

    def host_event(self):
        print("Hosting the adoption event...")
        for participant in self.participants:
            participant.adopt()
