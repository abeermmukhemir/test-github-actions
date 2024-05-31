from flask import Flask
from flask.typing import RouteCallable
from markupsafe import escape
from typing import NamedTuple

from hello.app_consts import APP_NAME


class Route(NamedTuple):
    rules: list[str]
    endpoint: str | None = None
    view_func: RouteCallable | None = None
    methods: list[str] | None = None


class Routes(object):
    """A wrapper to organize the API routes functionality
    """

    @property
    def ROUTES_MAP(self) -> list[Route]:
        """Map of each route and its facing function
        """
        return [
            Route(
                [
                    "/",
                    "/hello/",
                    "/hello/<string:hello_name>"
                ],
                "hello", self._hello),
            Route(
                [
                    "/hello-json/",
                    "/hello-json/<string:hello_name>"
                ],
                "hello-json", self._hello_json)
        ]

    def register_routes(self, app: Flask) -> None:
        """Register the API routes defined in the ROUTES_MAP to
        the "app" Flask object provided

        Args:
            app (Flask): Flask() object
        """
        for routes, endpoint, func, methods in self.ROUTES_MAP:
            for route in routes:
                app.add_url_rule(route,
                                 endpoint=endpoint,
                                 view_func=func,
                                 methods=methods)

    # For routes "/", "/hello/", "/hello/<string:hello_name>/"
    def _hello(self, hello_name: str | None = None):
        return self._construct_message(hello_name)

    # For routes "/hello-json/", "/hello-json/<string:hello_name>/"
    def _hello_json(self, hello_name: str | None = None):
        response = {
            "message": self._construct_message(hello_name)
        }
        return response

    def _construct_message(self, hello_name: str | None = None) -> str:
        # Helper function to construct a message to the user
        if not hello_name:
            hello_name = "there"
        message = "Hello {}!".format(escape(hello_name))
        return message


class Server(object):
    """A wrapper for Flask() object
    """

    def __init__(self, host: str = "127.0.0.1", port: str = "5000") -> None:
        """Initialize the server

        Args:
            host (str): Server IP address
            port (str): Server port number
        """
        self._host = host
        self._port = port

        self._flask_app = Flask(APP_NAME)

    def get_app_instance(self) -> Flask:
        return self._flask_app

    def register_routes(self) -> None:
        """Register the API routes
        """
        routes = Routes()
        routes.register_routes(self._flask_app)

    def run(self) -> None:
        """Starts the server
        """
        self._flask_app.run(self._host, self._port, debug=True)
