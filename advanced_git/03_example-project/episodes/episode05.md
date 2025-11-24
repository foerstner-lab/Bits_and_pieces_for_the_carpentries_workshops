<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 5 - Close Iteration 2

- Objective: Show minimal tasks to close the iteration
- Estimated time: 15min
- Teaching techniques: Live Demonstration

## Close the Iteration

### Preparation

- Explain that we only perform a minimal set as the details have not been defined yet (in the imaginary project)
- Create an issue via `Issues=>New Issue`

```
Name: Create release 0.2.0

Description:

## What is the purpose of the change?

- Tag current results 

## Which tasks have to be performed?

- [ ] Update changelog
- [ ] Create release tag

Assignee: Yourself
Milestone: Release 0.2.0
Label: type::release
```

### Update the Changelog

- Create merge request
- Update the changelog for release 0.2.0 via GitLab

```
## [Unreleased]()

## [0.2.0]() - YYY-MM-DD

### Added

- Added initial design addressing extensibility requirements including documentation and tests
- Provided implementation of the sum calculation
- Provided implementation of reading sample values from the command line
- Provided Makefile to automate tests, checks, and packaging
- Attached licensing (MIT, CC0-1.0) and copyright information
- Set up issue tracker
- Set up build pipeline
```

- Commit: "Update changelog for release 0.2.0"
- Merge the merge request (`Merge Requests`), remove `Closes`

### Create the Release Tag

- Create a tag via the `Repository => Tags => New Tag`, `New Tag`:

```
Tag name: 0.2.0
Description: Mark release 0.2.0
Release notes: Please see the [CHANGELOG](CHANGELOG.md) for further details.
```

> Releases in GitLab are currently improved (API, notifications). Please see the
> [GitLab Help on Releases](https://gitlab.com/help/user/project/releases/index.md)
> for further details.

- Show the GitLab Releases overview (`Project => Releases`)
- Tick all tasks in the release issue and close it
- Close the milestone (`Issues=>Milestones=>Select Milestone=>Close Milestone`)

## Key Points

- Properly mark your work as soon as you have reached a stable status.
- Tags / GitLab Releases help to make your project deliverables visible.
