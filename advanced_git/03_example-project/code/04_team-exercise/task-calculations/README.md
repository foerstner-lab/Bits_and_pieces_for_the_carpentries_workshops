<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Add further Calculations

In the following, we explain how to add the missing calculations.
You can find the prepared source code in the sub-directories.

> The implementation of the calculations average, variance, and standard deviation should be performed this order.
> Thus, please talk to the other teams to avoid unnecessary conflicts.
> All other calculations do not have any specific dependencies on each other.

## Preparation

- Create a corresponding issue using the `Change` template and add all relevant information (title, description, assignee, label, milestone).
- Create a merge request from the issue and edit it:
  - Use the `Review` template
  - Set the issue ID in the merge request description (e.g., `Fix #1`)
- Clone the Git repository and switch to the new branch.

## Add the Calculation and its Tests

- Copy the calculation `<Calculation Name>_calculation.py` into the directory `sample_calculator/calculations/calculations`.
- Copy the corresponding test `<Calculation Name>_calculation_test.py` into the directory `tests/calculations/calculations`.

## Integrate the new calculation

- Edit the file `sample_calculator/calculations/__init__.py` and add the corresponding import statement.
  The final list might look as follows:

```
from sample_calculator.calculations.calculations.average_calculation import AVERAGE_CALCULATION
from sample_calculator.calculations.calculations.deviation_calculation import DEVIATION_CALCULATION
from sample_calculator.calculations.calculations.median_calculation import MEDIAN_CALCULATION
from sample_calculator.calculations.calculations.median_high_calculation import MEDIAN_HIGH_CALCULATION
from sample_calculator.calculations.calculations.median_low_calculation import MEDIAN_LOW_CALCULATION
from sample_calculator.calculations.calculations.mode_unique_calculation import MODE_UNIQUE_CALCULATION
from sample_calculator.calculations.calculations.product_calculation import PRODUCT_CALCULATION
from sample_calculator.calculations.calculations.square_sum_calculation import SQUARE_SUM_CALCULATION
from sample_calculator.calculations.calculations.sum_calculation import SUM_CALCULATION
from sample_calculator.calculations.calculations.variance_calculation import VARIANCE_CALCULATION
```

- Edit the file `sample_calculator/main.py` and add the calculation constant to the list of calculations in the function `_perform_calculation`.
  The final list might look as follows:

```
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
```

> Please make sure that the `SUM_CALCULATION` is not part of the list.
> It should not be printed as part of the results.

## Integrate your Changes

### Commit and Push your Changes

- Commit locally and use a meaningful commit message.
- Push your changes.
- Make sure that the build pipeline ran successfully.

### Review the Changes

- A member of your team should perform the review.
- If everything is fine, approve the merge request.
  Otherwise correct the findings.

> The merge request cannot be approved by the merge request author.

### Merge the Changes

- Resolve the `WIP:` status and merge the changes.
- Make sure that:
  - The following build pipeline ran successfully.
  - Your feature branch has been deleted.
  - The issue has been closed.
