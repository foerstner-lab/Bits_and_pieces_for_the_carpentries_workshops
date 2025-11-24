# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Implements the variance calculation tests.
"""


import decimal
from unittest import mock

from sample_calculator import calculations
from sample_calculator.calculations.calculations import variance_calculation


class TestVarianceCalculation:
    def setup_method(self, _):
        self._average_mock = mock.Mock()
        self._average_mock.name = calculations.AVERAGE_CALCULATION
        self._average_mock.calculate = mock.Mock(return_value=decimal.Decimal(2))
        self._variance = variance_calculation.VarianceCalculation([self._average_mock], dict())

    def test_calculate_success(self):
        assert self._variance.calculate([decimal.Decimal(1), decimal.Decimal(2), decimal.Decimal(3)]) == 1

    def test_calculate_empty(self):
        self._average_mock.calculate.return_value = decimal.Decimal("NaN")
        assert self._variance.calculate([]).is_nan()

    def test_calculate_only_one_value(self):
        self._average_mock.calculate.return_value = decimal.Decimal(2)
        assert self._variance.calculate([decimal.Decimal(2)]).is_nan()
