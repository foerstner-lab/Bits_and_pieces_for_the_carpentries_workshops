# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Implements the unique mode calculation tests.
"""


import decimal

from sample_calculator.calculations.calculations import mode_unique_calculation


class TestModeUniqueCalculation:
    def setup_method(self, _):
        self._mode_unique = mode_unique_calculation.ModeUniqueCalculation(list(), dict())

    def test_calculate_success(self):
        assert self._mode_unique.calculate(
            [decimal.Decimal(4), decimal.Decimal(4), decimal.Decimal(1), decimal.Decimal(2)]
        ) == decimal.Decimal(4)

    def test_calculate_multimode(self):
        assert self._mode_unique.calculate([decimal.Decimal(2), decimal.Decimal(1), decimal.Decimal(3)]).is_nan()

    def test_calculate_empty(self):
        assert self._mode_unique.calculate([]).is_nan()
