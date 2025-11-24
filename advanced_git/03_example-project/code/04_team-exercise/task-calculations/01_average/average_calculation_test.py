# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Implements the average calculation tests.
"""


import decimal
from unittest import mock

from sample_calculator import calculations
from sample_calculator.calculations.calculations import average_calculation


class TestAverageCalculation:
    def setup_method(self, _):
        self._sum_mock = mock.Mock()
        self._sum_mock.name = calculations.SUM_CALCULATION
        self._sum_mock.calculate = mock.Mock(return_value=decimal.Decimal(6))
        self._average = average_calculation.AverageCalculation([self._sum_mock], dict())

    def test_calculate_success(self):
        assert self._average.calculate([decimal.Decimal(1), decimal.Decimal(2), decimal.Decimal(3)]) == 2

    def test_calculate_empty(self):
        self._sum_mock.calculate.return_value = 0
        assert self._average.calculate([]).is_nan()
