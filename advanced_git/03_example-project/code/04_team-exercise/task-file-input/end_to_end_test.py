# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Some tests to check that the 'sample_calculator' executable is working as expected.
"""


import subprocess
import sys

from sample_calculator import main

_DEFAULT_SHELL_ENCODING = sys.getdefaultencoding()


def test_input_from_console_success():
    _run_sample_calculator([], stdin="1;2;3", should_succeed=True)


def test_input_from_file_success(tmpdir):
    input_file = tmpdir.join("input.txt")
    input_file.write("1;2;3")
    parameters = ["--filepath", str(input_file)]
    _run_sample_calculator(parameters, stdin="", should_succeed=True)


def test_input_wrong_input_format():
    _run_sample_calculator([], stdin="WRONG", should_succeed=False)


def test_wrong_parameter():
    _run_sample_calculator(["-wrong_parameter"], stdin="", should_succeed=False)


def _run_sample_calculator(parameters, stdin="", should_succeed=True):
    # Run command
    command = [sys.executable, main.__file__] + parameters
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(stdin.encode(_DEFAULT_SHELL_ENCODING))
    stdout = stdout.decode(_DEFAULT_SHELL_ENCODING)
    stderr = stderr.decode(_DEFAULT_SHELL_ENCODING)

    # Print in case of error for debugging
    print(command)
    print(stdout)
    print(stderr)

    # Check results
    if should_succeed:
        assert process.returncode == 0
    else:
        assert process.returncode != 0
