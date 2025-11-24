# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Calculates the median (high) of the sample values.

In case of an even number of sample values the higher value is selected instead of performing an interpolation.
"""


import statistics

from sample_calculator.calculations import base

MEDIAN_HIGH_CALCULATION = "MEDIAN_HIGH"


class MedianHighCalculation(base.Calculation):
    """Calculates the median (high) of the sample values."""

    name = MEDIAN_HIGH_CALCULATION
    dependent_calculations = list()

    def _calculate(self, sample_values, dependent_values):
        return statistics.median_high(sample_values)
