

def test_flask_hello(client, file_regression):
    resp = client.get('/hello')
    assert resp.status_code == 200
    file_regression.check(resp.data.decode(), extension=".html", encoding="utf-8")
