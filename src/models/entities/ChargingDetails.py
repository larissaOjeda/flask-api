class ChargingDetails(): 

    def __init__(self, vin, id, startAt = None, endAt = None):
        self.vin = vin
        self.startAt = startAt
        self.endAt = endAt
        self.id = id

    def to_JSON(self):
        return {
            'vin' : self.vin, 
            'chargeStartAt' : self.startAt,
            'chargeEndAt' : self.endAt, 
            'id' : self.id
        }
    
    

    