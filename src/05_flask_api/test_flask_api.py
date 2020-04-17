

def test_heroes_item(client, data_regression):
    resp = client.get('/api/heroes/4')
    assert resp.status_code == 200
    data_regression.check(resp.get_json())


def test_heroes_collection(client, data_regression):
    resp = client.get('/api/heroes')
    assert resp.status_code == 200
    data_regression.check(resp.get_json())
