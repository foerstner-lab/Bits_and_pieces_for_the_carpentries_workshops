# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Calculates the standard deviation.
"""


import decimal

from sample_calculator.calculations import base
from sample_calculator.calculations.calculations.variance_calculation import VARIANCE_CALCULATION

DEVIATION_CALCULATION = "DEVIATION"


class DeviationCalculation(base.Calculation):
    """Calculates the standard deviation of the sample values."""

    name = DEVIATION_CALCULATION
    dependent_calculations = [VARIANCE_CALCULATION]

    def _calculate(self, sample_values, dependent_values):
        variance = dependent_values[VARIANCE_CALCULATION]
        return variance ** decimal.Decimal("0.5")
