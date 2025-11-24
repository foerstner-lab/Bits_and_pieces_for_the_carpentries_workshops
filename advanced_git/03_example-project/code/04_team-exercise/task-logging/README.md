<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Add Logging

In the following, we explain how to add the logging functionality.
You can find the prepared source code in this directory.

## Preparation

- Create a corresponding issue using the `Change` template and add all relevant information (title, description, assignee, label, milestone).
- Create a merge request from the issue and edit it:
  - Use the `Review` template (click on 'edit' in the merge request and Choose a template)
  - Set the issue ID in the merge request description (e.g., `Fix #1`)
- Clone the Git repository and switch to the new branch.

## Add the Logging Configuration

- Copy the directory `conf` into the directory `sample_calculator`.

## Integrate the Logging

- Copy the file `console_input.py` into the directory `sample_calculator/inputs/inputs` (overwrite it).
- Adapt the file `sample_calculator/main.py` as follows:

### Replace the Imports (in line 12)

```
import argparse
import sys
```

by: 

```
import argparse
import configparser
import logging
import os
import sys
from logging import config
```

### Add the Logging Constant (in line 23)

`_LOG = logging.getLogger()`

### Replace the following print Statements

- Replace (line 51):

`print("Cannot retrieve the sample values. Reason: %s" % error.args)`

by:

`_LOG.error("Cannot retrieve the sample values. Reason: %s", error.args)`

- Replace (line 53):

`print("Using the following sample values: %s" % sample_values)`

by:

`_LOG.info("Using the following sample values: %s", sample_values)`

- Replace (line 62):

`print("%s: %1.2f" % (calculation.name, result))`

by:

`_LOG.info("%s: %1.2f", calculation.name, result)`

### Add the _init_logger Function

- Replace (at the end of `main.py`):

```
def _init_logger():
    pass
```

by:

```
def _init_logger():
    logger_conf_file_path = os.path.join(os.path.dirname(__file__), "conf", "logger.conf")
    try:
        config.fileConfig(logger_conf_file_path)
    except (KeyError, configparser.Error) as error:
        print("Cannot use default and use a console logger instead. Reason: '{0}'". format(error))
        logging.root.addHandler(logging.StreamHandler(sys.stdout))
        logging.root.setLevel(logging.INFO)
```

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
