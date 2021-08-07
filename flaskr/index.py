from datetime import datetime

from flask import Blueprint, g, render_template

from flaskr.db import get_db

bp = Blueprint('index', __name__)

@bp.route('/')
def get():
    db = get_db()

    cur = db.cursor()

    quarter = f'q{datetime.now().time().minute // 15 + 1}'

    query = f'''SELECT campaign_id, COUNT(banner_id)
            FROM banners_with_conversions_{quarter}
            GROUP BY campaign_id
            '''

    cur.execute(query)
    campaigns = cur.fetchall()

    return render_template('index.html', campaigns=campaigns)
