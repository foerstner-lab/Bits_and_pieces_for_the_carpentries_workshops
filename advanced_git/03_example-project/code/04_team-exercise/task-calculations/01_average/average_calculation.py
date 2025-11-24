# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Calculates the average.
"""


from sample_calculator.calculations import base
from sample_calculator.calculations.calculations.sum_calculation import SUM_CALCULATION

AVERAGE_CALCULATION = "AVERAGE"


class AverageCalculation(base.Calculation):
    """Calculates the average of the sample values."""

    name = AVERAGE_CALCULATION
    dependent_calculations = [SUM_CALCULATION]

    def _calculate(self, sample_values, dependent_values):
        return dependent_values[SUM_CALCULATION] / len(sample_values)
