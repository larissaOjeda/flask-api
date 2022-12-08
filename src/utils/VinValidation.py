class VinValidation(): 

     @classmethod 
     def is_vin_valid(self, vin):
        return len(str(vin)) > 0
