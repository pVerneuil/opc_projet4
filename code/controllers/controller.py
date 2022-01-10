from tinydb import TinyDB, Query

db = TinyDB('data/db.json')
table = db.table('players_db')
table.insert({'test' : '3'})