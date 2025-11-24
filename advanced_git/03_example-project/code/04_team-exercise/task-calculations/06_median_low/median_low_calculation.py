# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Calculates the median (low) of the sample values.

In case of an even number of sample values the lower value is selected instead of performing an interpolation.
"""


import statistics

from sample_calculator.calculations import base

MEDIAN_LOW_CALCULATION = "MEDIAN_LOW"


class MedianLowCalculation(base.Calculation):
    """Calculates the median (low) of the sample values."""

    name = MEDIAN_LOW_CALCULATION
    dependent_calculations = list()

    def _calculate(self, sample_values, dependent_values):
        return statistics.median_low(sample_values)
