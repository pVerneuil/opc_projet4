from datetime import datetime
from logging import raiseExceptions
class Round : 
    def __init__(self, name, matches : list) -> None:
        self.name = name
        self.matches = matches
    
    def set_date_and_time(self, starting :bool):
       if starting: self.start_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
       if not starting: self.end_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
       if type(starting) != bool : 
           raise TypeError("can only take True or False (True to set the starting date&time; Fasle to set the end date&time)")