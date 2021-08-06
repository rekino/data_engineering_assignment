from flask import Blueprint, g, render_template

from flaskr.db import get_db

bp = Blueprint('index', __name__)

@bp.route('/')
def get():
    db = get_db()

    cur = db.cursor()

    cur.execute('SELECT DISTINCT campaign_id FROM impressions')
    campaigns = cur.fetchall()

    return render_template('index.html', campaigns=campaigns)
