import datetime
class DateFormat(): 

    @classmethod # to use it without creating an instance of it 
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')