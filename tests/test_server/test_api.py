import logging
import pytest


class TestAPIEndpoints:
    """Contains test cases for API endpoints.
    """
    @pytest.fixture
    def get_endpoint(self, client, endpoint):
        logging.debug("GET -> endpoint: {}".format(endpoint))
        if not endpoint:
            return client.get('/')
        return client.get(endpoint, follow_redirects=True)

    @pytest.fixture
    def status_ok(self, get_endpoint):
        logging.debug("Response status code: {}".format(get_endpoint.status))
        return get_endpoint.status == "200 OK"

    @pytest.fixture
    def status_not_found(self, get_endpoint):
        logging.debug("Response status code: {}".format(get_endpoint.status))
        return get_endpoint.status == "404 NOT FOUND"

    @pytest.mark.parametrize('endpoint',
                             ['', '/hello', '/hello/someone'])
    def test_hello(self, get_endpoint, status_ok, endpoint):
        response = get_endpoint
        assert status_ok
        url_parts = endpoint.split('/')
        if len(url_parts) == 3:
            expected = f'Hello {url_parts[-1]}!'
        else:
            expected = 'Hello there!'
        assert response.text == expected

    @pytest.mark.parametrize('endpoint', ['/hello-json', '/hello-json/someone'])
    def test_hello_json(self, get_endpoint, status_ok, endpoint):
        response = get_endpoint
        assert status_ok
        assert response.is_json
        url_parts = endpoint.split('/')
        expected = {}
        if len(url_parts) == 3:
            expected = {
                "message": f'Hello {url_parts[-1]}!'
            }
        else:
            expected = {
                "message": 'Hello there!'
            }
        assert response.json == expected

    @pytest.mark.parametrize('endpoint',
                             ['/foo', '/foo/bar', '/foo///',
                              '/hello/someone/foo', '/hello-json/someone/bar'])
    def test_wrong_endpoints(self, status_not_found):
        assert status_not_found
