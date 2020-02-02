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
