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
    quarter = datetime.now().time().minute // 15 + 1

    db = get_db()

    cur = db.cursor()

    query = '''
                SELECT
                    impressions.banner_id AS banner_id, 
                    COUNT(clicks.click_id) AS clicks, 
                    COUNT(conversions.conversion_id) AS conversions 
                FROM impressions 
                LEFT JOIN clicks ON impressions.campaign_id = clicks.campaign_id AND impressions.banner_id = clicks.banner_id
                LEFT JOIN conversions ON clicks.click_id = conversions.click_id
                WHERE impressions.campaign_id=%s AND (clicks.quarter = %s OR clicks.quarter IS NULL)
                GROUP BY impressions.banner_id
                ORDER BY conversions DESC, clicks DESC;
            '''
    cur.execute(query, (campaign_id, quarter))

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