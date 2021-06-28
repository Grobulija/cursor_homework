from tests.conftest import client


def test_article_create(client):
    response = client.get('/article/create')
    data = response.json
    assert response.status_code == 200

    headers = {
        "Content-Type": "application/json"
    }

    json = {
        "title": "Test Article",
        "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
        "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
        "description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
        "slug": "test-article",
        "author_id": "-1"
    }
    response = client.post("/article/store", headers=headers, json=json)
    assert response.status_code == 500
