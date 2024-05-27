import argparse

from hello.app_consts import APP_NAME, APP_VERSION

# Help message constants
PROG_STR = "Simple Hello World webapp using flask"
VERSION_ARG_HELP = "App version"
RUN_ACTION_HELP = "Run the server"
HOST_ARG_DEFAULT = "127.0.0.1"
HOST_ARG_HELP = f"IP address for the server. Defaults to {HOST_ARG_DEFAULT}"
PORT_ARG_DEFAULT = "5000"
PORT_ARG_HELP = f"Port number for the server. Defaults to {PORT_ARG_DEFAULT}"


def parse_args(args_list: list) -> dict:
    """Parse provided arguments for the application

    Args:
        args_list (list): List of args to parse, should be in a Unix/Linux
            based style, for example:
            ["--host", "x.x.x.x", "--port", "yyyy"]

    Returns:
        (dict): If parsing is successful a dict is returned with the keys being:
                host (str), port (str)
    """

    parser = argparse.ArgumentParser(prog=APP_NAME, description=PROG_STR)
    parser.add_argument("-v", "--version", action='version',
                        version=APP_VERSION, help=VERSION_ARG_HELP)
    sub_parsers = parser.add_subparsers(required=True)
    run_parser = sub_parsers.add_parser("run", help=RUN_ACTION_HELP,
                                        description=RUN_ACTION_HELP)
    run_parser.add_argument("--host", type=str,
                            default=HOST_ARG_DEFAULT, help=HOST_ARG_HELP)
    run_parser.add_argument("--port", type=str,
                            default=PORT_ARG_DEFAULT, help=PORT_ARG_HELP)

    args = parser.parse_args(args_list)
    args = {
        "host": args.host,
        "port": args.port
    }
    return args
