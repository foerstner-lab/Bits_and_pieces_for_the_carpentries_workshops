# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Calculates the median of the sample values.
"""


import statistics

from sample_calculator.calculations import base

MEDIAN_CALCULATION = "MEDIAN"


class MedianCalculation(base.Calculation):
    """Calculates the median of the sample values."""

    name = MEDIAN_CALCULATION
    dependent_calculations = list()

    def _calculate(self, sample_values, dependent_values):
        return statistics.median(sample_values)
