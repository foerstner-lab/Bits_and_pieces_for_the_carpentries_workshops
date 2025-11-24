# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Calculates the unique mode of the sample values.
"""


import decimal
import statistics

from sample_calculator.calculations import base

MODE_UNIQUE_CALCULATION = "MODE_UNIQUE"


class ModeUniqueCalculation(base.Calculation):
    """Calculates the unique mode of the sample values."""

    name = MODE_UNIQUE_CALCULATION
    dependent_calculations = list()

    def _calculate(self, sample_values, dependent_values):
        # The semantics of "statistics.mode" changed in Python 3.8.
        # For that reason, we have to make sure that our implementation works consistently
        # across all supported Python versions.
        # See also: https://docs.python.org/3/library/statistics.html#statistics.mode
        if hasattr(statistics, "multimode"):
            modes = statistics.multimode(sample_values)
            if len(modes) == 1:
                return modes[0]
            else:
                return decimal.Decimal("NaN")
        else:
            try:
                return statistics.mode(sample_values)
            except statistics.StatisticsError:
                return decimal.Decimal("NaN")
