# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Implements the file input method tests.
"""


import decimal

import pytest

from sample_calculator.inputs import base
from sample_calculator.inputs.inputs import file_input


def test_get_input_values_success(tmpdir):
    # Setup
    input_file = tmpdir.join("input.txt")
    input_file.write("1;2;3")
    file_input_method = file_input.FileInputMethod(str(input_file))

    # Run and check result
    assert file_input_method.get_input_values() == [decimal.Decimal(1), decimal.Decimal(2), decimal.Decimal(3)]


def test_get_input_values_multiple_lines(tmpdir):
    # Setup
    input_file = tmpdir.join("input.txt")
    input_file.write("1;2;3;\n590.0;56.0\n;1;2")
    file_input_method = file_input.FileInputMethod(str(input_file))

    # Run and check result
    assert file_input_method.get_input_values() == [
        decimal.Decimal(1),
        decimal.Decimal(2),
        decimal.Decimal(3),
        decimal.Decimal(590.0),
        decimal.Decimal(56.0),
        decimal.Decimal(1),
        decimal.Decimal(2),
    ]


def test_get_input_values_invalid_filepath(tmpdir):
    # Setup
    nonexistent_file = tmpdir.join("it-does-not-exist.txt")
    file_input_method = file_input.FileInputMethod(str(nonexistent_file))

    # Run and check result
    with pytest.raises(base.InputMethodError):
        file_input_method.get_input_values()


def test_get_input_values_invalid_content(tmpdir):
    # Setup
    input_file = tmpdir.join("input.txt")
    input_file.write("12;INVALID;12;23")
    file_input_method = file_input.FileInputMethod(str(input_file))

    # Run and check result
    with pytest.raises(base.InputMethodError):
        file_input_method.get_input_values()
