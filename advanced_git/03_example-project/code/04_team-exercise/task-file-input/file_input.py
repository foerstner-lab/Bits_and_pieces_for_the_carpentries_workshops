# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Reads the sample values from a CSV file.
"""


import decimal

from sample_calculator.inputs import base, inputs

FILE_INPUT = "FILE"


class FileInputMethod(base.InputMethod):
    """Reads the sample values from a file.
    Values should be separated by semicolon.
    """

    name = FILE_INPUT

    def __init__(self, filepath=None):
        self._filepath = filepath

    def get_input_values(self):
        conversion_error = None
        values = list()
        try:
            with open(self._filepath, "r") as file_object:
                for line in file_object:
                    try:
                        for value in line.split(inputs.SPLIT_CHARACTER):
                            if value.strip():
                                values.append(decimal.Decimal(value))
                    except decimal.InvalidOperation as error:
                        conversion_error = error
                        break
        except IOError as error:
            raise base.InputMethodError("Cannot access file '{0}'. Reason: {1}".format(self._filepath, error.args))
        if conversion_error is not None:
            raise base.InputMethodError("Invalid input provided. Details: {0}".format(conversion_error.args))
        return values
