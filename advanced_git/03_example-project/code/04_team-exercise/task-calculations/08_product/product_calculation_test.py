# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Implements the product calculation tests.
"""


import decimal

from sample_calculator.calculations.calculations import product_calculation


class TestProductCalculation:
    def setup_method(self, _):
        self._product = product_calculation.ProductCalculation(list(), dict())

    def test_calculate_success(self):
        assert (
            self._product.calculate([decimal.Decimal(1), decimal.Decimal(2), decimal.Decimal(3), decimal.Decimal(4)])
            == 24
        )

    def test_calculate_empty(self):
        assert self._product.calculate([]).is_nan()

    def test_calculate_with_zero(self):
        assert (
            self._product.calculate([decimal.Decimal(1), decimal.Decimal(2), decimal.Decimal(3), decimal.Decimal(0)])
            == 0
        )
