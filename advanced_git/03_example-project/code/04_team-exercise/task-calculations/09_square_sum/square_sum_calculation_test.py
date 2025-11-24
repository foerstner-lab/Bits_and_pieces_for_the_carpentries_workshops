# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Implements the square sum calculation tests.
"""


import decimal

from sample_calculator.calculations.calculations import square_sum_calculation


class TestSquareSumCalculation:
    def setup_method(self, _):
        self._square_sum = square_sum_calculation.SquareSumCalculation(list(), dict())

    def test_calculate_success(self):
        assert self._square_sum.calculate([decimal.Decimal(1), decimal.Decimal(2), decimal.Decimal(3)]) == 14

    def test_calculate_empty(self):
        assert self._square_sum.calculate([]).is_nan()
