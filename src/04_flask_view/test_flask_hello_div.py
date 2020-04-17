from bs4 import BeautifulSoup


def test_flask_hello_div(client, file_regression):
    resp = client.get('/')
    assert resp.status_code == 200

    soup = BeautifulSoup(resp.data.decode(), 'html.parser')
    main_div_element = soup.select_one('.starter-header')
    file_regression.check(str(main_div_element), extension=".html")
