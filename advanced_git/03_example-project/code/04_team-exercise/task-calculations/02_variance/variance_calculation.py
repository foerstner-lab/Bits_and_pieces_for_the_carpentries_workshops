# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Calculates the variance.
"""


import decimal

from sample_calculator.calculations import base
from sample_calculator.calculations.calculations.average_calculation import AVERAGE_CALCULATION

VARIANCE_CALCULATION = "VARIANCE"


class VarianceCalculation(base.Calculation):
    """Calculates the variance value of the sample values."""

    name = VARIANCE_CALCULATION
    dependent_calculations = [AVERAGE_CALCULATION]

    def _calculate(self, sample_values, dependent_values):
        if len(sample_values) < 2:
            return decimal.Decimal("NaN")

        average = dependent_values[AVERAGE_CALCULATION]
        variance = 0
        for sample_value in sample_values:
            variance += (sample_value - average) ** 2
        return variance / (len(sample_values) - 1)
