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

    query = f'''SELECT SUM(clicks), SUM(conversions)
            FROM banners_with_conversions_{quarter}
            WHERE campaign_id=%s
            '''

    cur.execute(query, (campaign_id, ))

    clicks, conversions = cur.fetchone()

    size = 5

    if conversions >= 10:
        size = 10
    
    if conversions in range(5, 10):
        size = conversions

    query = f'''SELECT banner_id
            FROM banners_with_conversions_{quarter}
            WHERE campaign_id=%s
            ORDER BY conversions DESC, clicks DESC
            '''
    cur.execute(query, (campaign_id, ))

    if conversions == 0 and clicks < 5:
        banners = cur.fetchall()
        top, bottom = banners[:clicks], banners[clicks:]
        random.shuffle(bottom)
        banners = top + bottom[:5-clicks]
    else:
        banners = cur.fetchmany(size=size)
        
    random.shuffle(banners)

    banner = banners.pop()[0]
    last_banner = get_dict()
    if last_banner[request.remote_addr] == banner:
        banner = banners.pop()[0]
    last_banner[request.remote_addr] = banner

    campaign = Campaign(id=campaign_id, banner=f'images/image_{banner}.png')
    return render_template('campaigns/campaign.html', campaign=campaign)