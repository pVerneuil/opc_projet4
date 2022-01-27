from tinydb import TinyDB, Query

db = TinyDB("data/db.json")
players_table = db.table("players")
tournament_table = db.table("tournament")


class DataController:
    def add_one_to_db(data, table):
        table.insert(data)

    def add_many_to_db(data, table):
        table.insert_multiple(data)

    def fetch_all_data_from_table(table):
        return table.all()

    def get_document_by_id(table, id):
        return table.get(doc_id=id)
