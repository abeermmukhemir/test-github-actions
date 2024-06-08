import pytest
from hello.server import Server


@pytest.fixture
def app():
    server = Server()
    server.register_routes()
    app = server.get_app_instance()
    app.config.update({
        "TESTING": True,
    })
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
