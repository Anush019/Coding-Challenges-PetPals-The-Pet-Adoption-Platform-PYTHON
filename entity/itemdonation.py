from entity.donation import donation

class itemdonation(donation):
    def __init__(self,donar_name,amount,itemtype):
        super().__init__(donar_name,amount)
        self._itemtype=itemtype

    def get_itemtype(self):
        return self._itemtype

    def set_itemtype(self,itemtype):
        self._itemtype=itemtype

