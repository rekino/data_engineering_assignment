from flask import Blueprint, g, render_template

from flaskr.db import get_db

bp = Blueprint('campaign', __name__, url_prefix='/campaigns')

@bp.route('/<int:campaign_id>')
def get(campaign_id):
    return render_template('campaigns/campaign.html', campaign=campaign_id)