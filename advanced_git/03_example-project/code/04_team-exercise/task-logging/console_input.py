# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Reads sample values from console.
"""


import decimal
import logging
import sys

from sample_calculator.inputs import base, inputs

CONSOLE_INPUT = "CONSOLE"

_LOG = logging.getLogger()


class ConsoleInputMethod(base.InputMethod):
    """Reads a single line from the console.
    Values should be separated by semicolon.
    """

    name = CONSOLE_INPUT

    def get_input_values(self):
        _LOG.info("Insert the sample values (separated by ';'): ")
        values = sys.stdin.readline()
        try:
            return [decimal.Decimal(value) for value in values.split(inputs.SPLIT_CHARACTER) if value.strip()]
        except decimal.InvalidOperation as error:
            raise base.InputMethodError("Invalid input provided. Details: {0}".format(error.args))
