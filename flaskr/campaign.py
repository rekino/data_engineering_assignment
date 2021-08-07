from collections import namedtuple, defaultdict
from datetime import datetime
import random

from flask import Blueprint, g, render_template, request

from flaskr.db import get_db

Campaign = namedtuple('Campaign', 'id banner')

bp = Blueprint('campaign', __name__, url_prefix='/campaigns')

def get_dict():
    if 'dict' not in g:
        g.dict = defaultdict(list)
    
    return g.dict

@bp.route('/<int:campaign_id>')
def get(campaign_id):
    quarter = f'q{datetime.now().time().minute // 15 + 1}'

    db = get_db()

    cur = db.cursor()

    query = f'''SELECT banner_id, clicks, conversions
            FROM banners_with_conversions_{quarter}
            WHERE campaign_id=%s
            ORDER BY conversions DESC, clicks DESC
            '''
    cur.execute(query, (campaign_id, ))

    rows = cur.fetchall()

    banners = []
    for i in range(10):
        row = rows[0]
        if row[2] > 0:
            banners.append(rows.pop(0))
        elif i > 4:
            break
        elif row[1] > 0:
            banners.append(rows.pop(0))
        else:
            banners.append(rows.pop(random.randint(0, len(rows) - 1)))

    random.shuffle(banners)
    banner = banners.pop()[0]
    last_banner = get_dict()
    if last_banner[request.remote_addr] == banner:
        banner = banners.pop()[0]
    last_banner[request.remote_addr] = banner

    campaign = Campaign(id=campaign_id, banner=f'images/image_{banner}.png')
    return render_template('campaigns/campaign.html', campaign=campaign)