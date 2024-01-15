class Reservation:

    def __init__(self, id, accountId, tableId, startAt, endAt, status, feedback=None):
        self.id = id
        self.accountId = accountId
        self.tableId = tableId
        self.startAt = startAt
        self.endAt = endAt
        self.status = status
        self.feedback = feedback

    def toJSON(self):
        return {
            "id": self.id,
            "accountId": self.accountId,
            "tableId": self.tableId,
            "startAt": self.startAt,
            "endAt": self.endAt,
            "status": self.status
        }

    def toJSONWithoutAccountId(self):
        return {
            "id": self.id,
            "tableId": self.tableId,
            "startAt": self.startAt,
            "endAt": self.endAt,
            "status": self.status,
            "feedback": self.feedback
        }
    
    def toJSONWithoutTableId(self):
        return {
            "id": self.id,
            "accountId": self.accountId,
            "startAt": self.startAt,
            "endAt": self.endAt,
            "status": self.status
        }