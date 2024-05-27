import sys

from hello.args_parser import parse_args
from hello.server import Server


def main(args: list | None = None):
    """Entry point for the application, this will
    1) parse provided input arguments and configs
    2) initialize the server with givin config
    3) bind the API endpoints to the server instance
    4) start the server

    Args:
        args (list|None): list of input args in a Unix/Linux based style
            for example:
            ["--host", "x.x.x.x", "--port", "yyyy"]
            if not provided will use sys.argv
    """
    if args is None:
        args = sys.argv[1:]
    args_parsed = parse_args(args)

    server = Server(
        host=args_parsed["host"],
        port=args_parsed["port"])

    server.register_routes()
    server.run()


if __name__ == "__main__":
    main()
