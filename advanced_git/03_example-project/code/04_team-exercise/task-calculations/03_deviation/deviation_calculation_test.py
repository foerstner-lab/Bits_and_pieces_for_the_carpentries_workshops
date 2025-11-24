# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Implements the deviation calculation tests.
"""


import decimal
from unittest import mock

from sample_calculator import calculations
from sample_calculator.calculations.calculations import deviation_calculation


class TestDeviationCalculation:
    def setup_method(self, _):
        self._variance_mock = mock.Mock()
        self._variance_mock.name = calculations.VARIANCE_CALCULATION
        self._variance_mock.calculate = mock.Mock(return_value=decimal.Decimal(1))
        self._deviation = deviation_calculation.DeviationCalculation([self._variance_mock], dict())

    def test_calculate_success(self):
        assert self._deviation.calculate([decimal.Decimal(1), decimal.Decimal(2), decimal.Decimal(3)]) == 1

    def test_calculate_empty(self):
        self._variance_mock.calculate.return_value = decimal.Decimal("NaN")
        assert self._deviation.calculate([]).is_nan()
