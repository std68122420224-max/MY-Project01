class Juice:
    def __init__(
            self,
            id :int,
            name :str,
            price :int):
        self.id = id
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f'<Juice: {self.name}>'