from database.db import get_connection
from .entities.ChargingDetails import ChargingDetails

from datetime import datetime


class ChargingDetailsModel():

    @classmethod
    def get_all(self): 
        try:
            connection = get_connection()
            chargingDetails = []

            with connection.cursor() as cursor: 
                query = 'SELECT * FROM charging_details ORDER BY vin ASC'
                cursor.execute(query)
                resultset = cursor.fetchall()

                for row in resultset: 
                    chargeDetail = ChargingDetails(row[0], row[1], row[2], row[3])
                    chargingDetails.append(chargeDetail.to_JSON())
            
            connection.close()
            return chargingDetails
        except Exception as ex: 
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, id): 
        try:
            connection = get_connection()

            with connection.cursor() as cursor: 
                cursor.execute('SELECT * FROM charging_details WHERE id = %s', (id,))
                row = cursor.fetchone()

                charging_detail = None
                if row != None:
                    charging_detail = ChargingDetails(row[0], row[1], row[2], row[3])
                    charging_detail = ChargingDetails.to_JSON()
            
            connection.close()
            return charging_detail
        except Exception as ex: 
            raise Exception(ex)
    
    @classmethod
    def create_charging_detail(self, charging_detail):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO charging_details (vin, charge_end_at, id) 
                                VALUES (%s, %s, %s)""", (charging_detail.vin, None, charging_detail.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_charging_detail(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE charging_details SET charge_end_at = %s
                                WHERE id = %s""", (datetime.now().utcnow(), id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    



    
