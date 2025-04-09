from abc import ABC,abstractmethod

class donation(ABC):
    def __init__(self, donor_name, amount):
        self._donor_name = donor_name
        self._amount = amount

    def get_donor_name(self):
        return self._donor_name

    def set_donor_name(self, donor_name):
        self._donor_name = donor_name

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    @abstractmethod
    def record_donation(self):
        pass
