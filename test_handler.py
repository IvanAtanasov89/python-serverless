from handler import hello


def test_hello():
    response = hello(None, None)
    print(response)
    assert response == {'body': '{"message": "\\u001b[31mHELLO"}', 'statusCode': 200}
