from controllers.data_controller import *

class Testing:
    
    def add_many_fake_player_to_db(a:int):
        i = 1
        dict = []
        for y in range(0,a):
            b=2000+i
            c=1000+i
            dict.append({"first_name": f"john{i}", "last_name": f"doe{i}", "date_of_birth": f"01/01/{b}", "gender": "M", "ranking": int(f"{c}")})
            i+=1
        DataController.add_many_to_db(dict, players_table)
