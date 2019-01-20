from hello.handler import hello


def test_hello():
    response = hello(None, None)
    assert response == {'body': '\x1b[31mHELLO', 'statusCode': 200}
