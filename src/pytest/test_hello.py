
def test_hello(client):
    response = client.get('/hello/')
    print(response.data)
    assert response.data == b'Hello there!'
