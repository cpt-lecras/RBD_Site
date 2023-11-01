from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import request, render_template
from sqlalchemy import desc
from Database import database_main as database
from Database.database_main import Ord

db=database.Session()

def show_table():
    users = db.query(database.Client).all()
    for user in users:
        print(user.id_client, user.nick)

def paginate(query, page, per_page=20):
    offset = (page - 1) * per_page
    total = query.order_by(None).count()

    items = query.limit(per_page).offset(offset).all()

    return items, total
def show_orders(user_id):
    page = request.args.get('page', 1, type=int)
    query = db.query(Ord).filter_by(id_client=user_id)
    orders, total = paginate(query, page, per_page=5)
    return render_template('orders.html', orders=orders, total=total, page=page, per_page=5)