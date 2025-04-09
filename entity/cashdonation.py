from datetime import datetime

class cashdonation:
    def __init__(self, donor, amount, donation_date=None):
        self._donor = donor
        self._amount = amount
        self._donation_date = donation_date if donation_date else datetime.now()

    def get_donor(self):
        return self._donor

    def get_amount(self):
        return self._amount

    def get_donation_date(self):
        return self._donation_date
