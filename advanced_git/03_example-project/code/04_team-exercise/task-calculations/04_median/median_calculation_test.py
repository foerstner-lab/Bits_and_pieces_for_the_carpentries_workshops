# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Implements the median calculation tests.
"""


import decimal

from sample_calculator.calculations.calculations import median_calculation


class TestMedianCalculation:
    def setup_method(self, _):
        self._median = median_calculation.MedianCalculation(list(), dict())

    def test_calculate_even(self):
        assert self._median.calculate(
            [decimal.Decimal(4), decimal.Decimal(1), decimal.Decimal(3), decimal.Decimal(2)]
        ) == decimal.Decimal(2.5)

    def test_calculate_uneven(self):
        assert self._median.calculate([decimal.Decimal(2), decimal.Decimal(1), decimal.Decimal(3)]) == decimal.Decimal(
            2
        )

    def test_calculate_empty(self):
        assert self._median.calculate([]).is_nan()
