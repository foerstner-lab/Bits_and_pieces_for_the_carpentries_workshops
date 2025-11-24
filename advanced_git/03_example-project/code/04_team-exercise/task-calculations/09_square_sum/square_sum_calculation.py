# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Calculates the square sum of the sample values.
"""


from sample_calculator.calculations import base

SQUARE_SUM_CALCULATION = "SQUARE_SUM"


class SquareSumCalculation(base.Calculation):
    """Calculates the square sum of all sample values."""

    name = SQUARE_SUM_CALCULATION
    dependent_calculations = list()

    def _calculate(self, sample_values, dependent_values):
        return sum(value * value for value in sample_values)
