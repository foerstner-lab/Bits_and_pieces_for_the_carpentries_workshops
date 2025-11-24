# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Implements the median (high) calculation tests.
"""


import decimal

from sample_calculator.calculations.calculations import median_high_calculation


class TestMedianHighCalculation:
    def setup_method(self, _):
        self._median_high = median_high_calculation.MedianHighCalculation(list(), dict())

    def test_calculate_even(self):
        assert self._median_high.calculate(
            [decimal.Decimal(4), decimal.Decimal(1), decimal.Decimal(3), decimal.Decimal(2)]
        ) == decimal.Decimal(3)

    def test_calculate_uneven(self):
        assert self._median_high.calculate(
            [decimal.Decimal(2), decimal.Decimal(1), decimal.Decimal(3)]
        ) == decimal.Decimal(2)

    def test_calculate_empty(self):
        assert self._median_high.calculate([]).is_nan()
