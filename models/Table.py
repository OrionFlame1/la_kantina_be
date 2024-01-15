class Table:

    def __init__(self, id, x, y, slots, reservations):
        self.id = id
        self.x = x
        self.y = y
        self.slots = slots
        self.reservations = [] if reservations is None else reservations

    def toJSON(self):
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "slots": self.slots,
            "reservations": self.reservations
        }