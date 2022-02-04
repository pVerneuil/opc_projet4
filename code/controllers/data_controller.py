from tinydb import *

db = TinyDB("data/db.json")
players_table = db.table("players")
tournament_table = db.table("tournament")


class DataController:
    def add_one_to_db(data, table):
        return table.insert(data)

    def add_many_to_db(data, table):
        return table.insert_multiple(data)

    def fetch_all_data_from_table(table):
        return table.all()

    def get_document_by_id(table, id):
        return table.get(doc_id=id)

    def get_documents_by_ids(table, ids: list):
        documents = []
        for id in ids:
            documents.append(DataController.get_document_by_id(table, id))
        return documents

    def update_by_id(table, data, id):
        """update table by ID

        Args:
            table (any): name of the table to update
            data (dictionary): contain the key of the value to update and the new value (ex: {'value':2})
            id (int): id of the item to update and
        """
        table.update(data, doc_ids=[id])
