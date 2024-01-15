class User:

    def __init__(self, id, name, role, points, reservations=[]):
        self.id = id
        self.name = name
        self.role = role
        self.points = points
        self.reservations = reservations

    def toJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.role,
            "points": self.points,
            "reservations": self.reservations
        }

    def toJSONWithNameAndReservation(self):
        return {
            "name": self.name,
            "reservations": self.reservations
        }

    def withReservations(self, reservations):
        self.reservations = reservations
        return self
