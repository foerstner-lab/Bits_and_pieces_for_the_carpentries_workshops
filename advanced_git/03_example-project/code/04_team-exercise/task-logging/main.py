# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


"""
This module is the central entry point of the application.
It initiates input methods, calculations, and the logging
capabilities.
"""


import argparse
import configparser
import logging
import os
import sys
from logging import config

from sample_calculator import calculations, inputs

_SUCCESS = 0
_ERROR = -1
_LOG = logging.getLogger()


def perform_calculation(inputmethod_name, *im_args, **im_kwargs):
    """Reads the sample values from the specified source. Then it performs the given
    calculations. I.e. it links the InputMethods and Calculations with each other.

    :param inputmethod_name: InputMethod constants.
    :param im_args: Additional arguments which might be required for the InputMethod.
    :param im_kwargs: Additional keyword arguments which might be required for the InputMethod.

    :returns: Error code. 0: indicates success / -1: indicates an error.
    """

    sample_values = _retrieve_sample_values(inputmethod_name, *im_args, **im_kwargs)
    if sample_values is not None:
        return_code = _perform_calculation(sample_values)
    else:
        return_code = _ERROR
    return return_code


def _retrieve_sample_values(inputmethod_name, *im_args, **im_kwargs):
    sample_values = None
    inputmethod = inputs.create_inputmethod(inputmethod_name, *im_args, **im_kwargs)
    try:
        sample_values = inputmethod.get_input_values()
    except inputs.InputMethodError as error:
        _LOG.error("Cannot retrieve the sample values. Reason: %s", error.args)
    else:
        _LOG.info("Using the following sample values: %s", sample_values)
    return sample_values


def _perform_calculation(sample_values):
    return_code = _SUCCESS
    calculations_ = calculations.create_calculation(
        [
            calculations.AVERAGE_CALCULATION,
            calculations.VARIANCE_CALCULATION,
            calculations.DEVIATION_CALCULATION,
            calculations.MEDIAN_CALCULATION,
            calculations.MEDIAN_LOW_CALCULATION,
            calculations.MEDIAN_HIGH_CALCULATION,
            calculations.MODE_UNIQUE_CALCULATION,
            calculations.SQUARE_SUM_CALCULATION,
            calculations.PRODUCT_CALCULATION,
        ]
    )
    for calculation in calculations_:
        result = calculation.calculate(sample_values)
        _LOG.info("%s: %1.2f", calculation.name, result)
    return return_code


def cmd_main():
    """Entry point of the command line tool. The executable script is generated
    by distribute library. See the entry_points definition in setup.py."""

    args = _parse_cmd_args()
    _init_logger()
    if args.filepath is not None:
        result = perform_calculation(inputs.FILE_INPUT, args.filepath)
    else:
        result = perform_calculation(inputs.CONSOLE_INPUT)
    sys.exit(result)


def _parse_cmd_args():
    parser = argparse.ArgumentParser(
        description="Calculates average, variance, and standard deviation of the given sample values."
    )
    parser.add_argument("--filepath", type=str, help="Path to the file which contains the sample values.")
    return parser.parse_args()


def _init_logger():
    logger_conf_file_path = os.path.join(os.path.dirname(__file__), "conf", "logger.conf")
    try:
        config.fileConfig(logger_conf_file_path)
    except (KeyError, configparser.Error) as error:
        print("Cannot use default and use a console logger instead. Reason: '{0}'".format(error))
        logging.root.addHandler(logging.StreamHandler(sys.stdout))
        logging.root.setLevel(logging.INFO)


if __name__ == "__main__":
    cmd_main()
