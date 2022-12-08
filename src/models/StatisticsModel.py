from database.db import get_connection
from .entities.ChargingDetails import ChargingDetails

from datetime import datetime
import pandas as pd
from pandas import DataFrame
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


class StatisticsModel():
    
    @classmethod
    def execute_query(self):
        try:
            connection = get_connection()

            with connection.cursor() as cursor: 
                query = 'SELECT * FROM charging_details ORDER BY vin ASC'
                cursor.execute(query)
                resultset = cursor.fetchall()

            connection.close()
            return resultset

        except Exception as ex: 
            raise Exception(ex)
                
    @classmethod
    def generate_statistics(self):
        try:
            cursor = self.execute_query()

            #Create the dataframe based on the query results and closing connection
            col_names = ['vin', 'start_at', 'end_at', 'id']
            df = DataFrame(cursor, columns=col_names)

            stats = {}
            df['time'] = (df.end_at - df.start_at).dt.total_seconds()
            stats = {
                'mean_time' : df.time.mean(), 
                'max_time' : df.time.max(),
                'description' : df.describe(include='O').to_dict('dict')
            }
            return stats 

        except Exception as ex: 
            raise Exception(ex)
    
    @classmethod
    def generate_plot(self): 
        try:
            cursor = self.execute_query()

            #Create the dataframe based on the query results and closing connection
            col_names = ['vin', 'start_at', 'end_at', 'id']
            df = DataFrame(cursor, columns=col_names)
            df['time'] = (df.end_at - df.start_at).dt.total_seconds()

            # Create the plot to visualize behavior of charging time 
            fig = Figure()
            axis = fig.add_subplot(1, 1, 1)
            axis.plot(df.vin, df.time)
            axis.set_xlabel('VIN')
            axis.set_ylabel('time in (s)')
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            return Response(output.getvalue(), mimetype='image/png')
            
        except Exception as ex: 
            raise Exception(ex)