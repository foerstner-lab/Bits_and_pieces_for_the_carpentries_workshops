<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Add the File Input

In the following, we explain how to add reading sample values from a file.
You can find the prepared source code in this directory.

## Preparation

- Create a corresponding issue using the `Change` template and add
  all relevant information (title, description, assignee, label, milestone).
- Create a merge request from the issue and edit it:
  - Use the `Review` template
  - Set the issue ID in the merge request description (e.g., `Fix #1`)
- Clone the Git repository and switch to the new branch.

## Add the file input and its tests

- Copy the module `file_input.py` into the directory `sample_calculator/inputs/inputs`.
- Copy the corresponding test `file_input_test.py` into the directory `tests/inputs/inputs`.
- Copy the file `end_to_end_test.py` into the directory `tests` (overwrite it).

## Integrate the file input

- Edit the file `sample_calculator/inputs/__init__.py`.
- Add the following import statement: `from sample_calculator.inputs.inputs.file_input import FILE_INPUT`
- Edit the file `sample_calculator/main.py`
- Adapt the function `cmd_main` and replace:

```
    if args.filepath is not None:
        pass
```

by: 

```
    if args.filepath is not None:
        result = perform_calculation(inputs.FILE_INPUT, args.filepath)
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
