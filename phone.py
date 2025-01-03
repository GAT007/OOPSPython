from item import Item
class Phone(Item):
    def __init__(self, name: str, price: int, quantity: int = 0, broken_phones: int = 0):
        #Call to super to have access to all of base class attributes/ methods
        super().__init__(
            name, price, quantity
        )
        #Do checks before assigning
        assert broken_phones>=0, f"{broken_phones} cannot be less than 0"

        #Assign to the instance variable
        self.broken_phones = broken_phones

    def __repr__(self):
            return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})"