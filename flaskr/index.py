from datetime import datetime

from flask import Blueprint, g, render_template

from flaskr.db import get_db

bp = Blueprint('index', __name__)

@bp.route('/')
def get():
    db = get_db()

    cur = db.cursor()

    query = '''SELECT campaign_id, COUNT(banner_id)
            FROM impressions
            GROUP BY campaign_id
            '''

    cur.execute(query)
    campaigns = cur.fetchall()

    return render_template('index.html', campaigns=campaigns)
