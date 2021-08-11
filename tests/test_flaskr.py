import os
import random

import pytest

import psycopg2

from flaskr import create_app
from flaskr.db import init_db
from flaskr.db import get_db

random.seed(1)

# read in SQL for populating test data
with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")

@pytest.fixture
def app():
    app = create_app({'TESTING': True, 'DATABASE': 'test'})

    with app.app_context():
        init_db()

        db = get_db()
        cur = db.cursor()
        cur.execute(_data_sql)

        db.commit()

    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(psycopg2.InterfaceError) as e:
        cur = db.cursor()

    assert "closed" in str(e.value)

@pytest.mark.parametrize("path", ("/", ))
def test_index(client, path):
    response = client.get(path)
    assert '<th>Campaign</th>' in str(response.data)

@pytest.mark.parametrize("path", ("/campaigns/1000", ))
def test_not_found(client, path):
    response = client.get(path)
    assert '<h1>The requested resource does not exists.</h1>' in str(response.data)

@pytest.mark.parametrize("path", ("/campaigns/1", ))
def test_X_gt_10(client, path):
    response = client.get(path)
    assert not 'image_111.png' in str(response.data)

@pytest.mark.parametrize("path", ("/campaigns/2", ))
def test_X_in_5_10(client, path):
    response = client.get(path)
    assert not 'image_106.png' in str(response.data)
    assert not 'image_107.png' in str(response.data)
    assert not 'image_108.png' in str(response.data)
    assert not 'image_109.png' in str(response.data)
    assert not 'image_110.png' in str(response.data)
    assert not 'image_111.png' in str(response.data)

@pytest.mark.parametrize("path", ("/campaigns/3", ))
def test_X_in_1_5(client, path):
    response = client.get(path)
    assert not 'image_106.png' in str(response.data)
    assert not 'image_107.png' in str(response.data)
    assert not 'image_108.png' in str(response.data)
    assert not 'image_109.png' in str(response.data)
    assert not 'image_110.png' in str(response.data)
    assert not 'image_111.png' in str(response.data)

@pytest.mark.parametrize("path", ("/campaigns/4", ))
def test_X_eq_0(client, path):
    response = client.get(path)
    assert 'image_101.png' in str(response.data)