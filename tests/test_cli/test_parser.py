import json
import logging
import pytest
import sys

from hello.app_consts import APP_VERSION
from hello.args_parser import parse_args, get_usage_message


class TestCLIArgs:
    """Contains test cases for command line interface.
    """
    test_data = [
        (
            'run',
            {
                "host": "127.0.0.1", "port": "5000"
            }
        ),
        (
            'run --host 0.0.0.0 --port 8080',
            {
                "host": "0.0.0.0", "port": "8080"
            }
        )
    ]

    @pytest.fixture
    def parsing_result(self, args, capsys):
        input_args = args.split()
        logging.debug("Input args: {}".format(input_args))
        try:
            parsed = parse_args(input_args)
            sys.stdout.write(json.dumps(parsed))
            exit_code = 0
        except SystemExit as sys_exit:
            exit_code = sys_exit.code

        out, err = capsys.readouterr()
        logging.debug(
            "Exit code: {}, stdout: {}, stderr: {}".format(
                exit_code, out, err))
        return exit_code, out, err

    @pytest.mark.parametrize('args',
                             [''])
    def test_no_args(self, parsing_result):
        exit_code, out, err = parsing_result
        assert exit_code == 2
        assert not out
        assert -1 != err.find(
            'error: the following arguments are required'
        )

    @pytest.mark.parametrize('args',
                             ['-h', '--help'])
    def test_help(self, parsing_result):
        exit_code, out, err = parsing_result
        assert not exit_code
        assert out == get_usage_message()
        assert not err

    @pytest.mark.parametrize('args',
                             ['-v', '--version'])
    def test_version(self, parsing_result):
        exit_code, out, err = parsing_result
        assert not exit_code
        assert out.strip() == APP_VERSION
        assert not err

    @pytest.mark.parametrize('args',
                             ['--foo'])
    def test_args_no_required(self, parsing_result):
        exit_code, out, err = parsing_result
        assert exit_code == 2
        assert not out
        assert -1 != err.find(
            'error: the following arguments are required'
        )

    @pytest.mark.parametrize('args',
                             ['run --foo'])
    def test_unknown_args(self, parsing_result):
        exit_code, out, err = parsing_result
        assert exit_code == 2
        assert not out
        assert -1 != err.find(
            'error: unrecognized arguments'
        )

    @pytest.mark.parametrize(('args', 'expected'), test_data)
    def test_command_run_args(self, parsing_result, expected):
        exit_code, out, err = parsing_result
        assert not exit_code
        actual = json.loads(out)
        assert actual == expected
        assert not err
