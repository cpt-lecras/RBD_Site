from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Database import database_main as database

db=database.Session()

def show_table():
    users = db.query(database.Client).all()
    for user in users:
        print(user.id_client, user.nick)