def test_server_check(client):
    response = client.get(
        '/',
    )
    data = response.json
    assert response.status_code == 200
    assert data['status']=='ready'