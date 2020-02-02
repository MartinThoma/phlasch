from urllib.parse import urlparse


async def test_shortener_shorten(cli, tables):
    response = await cli.post('/shortener/shorten', json={
        'address': 'https://google.com',
    })
    assert response.status == 201
    response_json = await response.json()
    assert response_json['shortcut'] == '1'
    assert urlparse(response_json['url']).path == '/1'


async def test_redirector_redirect(cli, tables):
    response = await cli.get('/1', allow_redirects=False)
    assert response.status == 302
    assert response.headers['Location'] == 'https://google.com'


async def test_stats_list(cli, tables):
    response = await cli.get('/stats/list')
    assert response.status == 200
    response_json = await response.json()
    assert response_json[0]['id'] == 1
    assert response_json[0]['address'] == 'https://google.com'
    assert response_json[0]['shortcut'] == '1'
    assert response_json[0]['visits'] == 1


async def test_stats_retrieve(cli, tables):
    response = await cli.get('/stats/retrieve/1')
    assert response.status == 200
    response_json = await response.json()
    assert response_json['id'] == 1
    assert response_json['address'] == 'https://google.com'
    assert response_json['shortcut'] == '1'
    assert response_json['visits'] == 1
