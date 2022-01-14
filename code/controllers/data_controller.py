from tinydb import TinyDB, Query

db = TinyDB("data/db.json")
players_table = db.table("players")


class DataController:
    def __init__(self) -> None:
        pass

    def add_one_to_db(self, data, table):
        table.insert({data})

    def add_many_to_db(self, data, table):
        table.insert_multiple({data})
