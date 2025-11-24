# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
Calculates the product of the sample values.
"""


from sample_calculator.calculations import base

PRODUCT_CALCULATION = "PRODUCT"


class ProductCalculation(base.Calculation):
    """Calculates the product of all sample values."""

    name = PRODUCT_CALCULATION
    dependent_calculations = list()

    def _calculate(self, sample_values, dependent_values):
        product = 1
        for value in sample_values:
            product = product * value
        return product
