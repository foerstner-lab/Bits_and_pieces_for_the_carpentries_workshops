<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 7 - Release Version 1.0.0

- Objective: Understand release management basics and how they can be applied in practice
- Estimated time: 30min
- Teaching techniques: Live Demonstration

## Explain the Release Management Basics

- Release number
- Release number schemes such as [semantic versioning](https://semver.org/) and [Calendar Versioning](https://calver.org/)
- Release package
- Changelog (Format: [Keep a Changelog](https://keepachangelog.com/))
- Release process:
  - Release planning
  - Release performance (major/minor release vs. bugfix release)
- For details, please see: 
  - [HIFIS Workshop: Bring Your Own Script and Make It Ready for Publication](https://gitlab.com/hifis/hifis-workshops/make-your-code-ready-for-publication/workshop-materials/-/blob/master/episodes/05_mark-the-stable-version-of-your-code.md)
  - [DLR Software Engineering Guidelines (Release Management)](https://rse.dlr.de/guidelines/00_dlr-se-guidelines_en.html#release-management)

## Explain the Release Process of the Example

- Show it in the developer guide
- Responsibility: Maintainers of the software
- Release number scheme: Semantic Versioning
- Changelog format: Keep a Changelog
- Release planning: milestones, issues
- Release process: release issues, release branches, release pipeline job, release tags


## Demonstrate the Release Process by creating Release 1.0.0

### Prepare the Release

- Create the issue to create the release using the `Release` template:

```
Title: Create release 1.0.0
Assignee: you
```

- Create the release merge request (branch name: `release/1.0.0`) from the issue
- Prepare the release as explained in the issue.
  At least, update the changelog as follows:

```
## [Unreleased]()

## [1.0.0]() - YYYY-MM-DD

### Added

- Added calculations: average, variance, deviation, ...
- Added reading sample values from CSV formatted files
- Added configurable logging
```

- Commit and push changes to the remote release branch
- Check the release using the checklist in the release issue

### Create the Release

- Tag the release branch via GitLab
- Merge the merge request
- Update the release notes (`Repository => Tags, Edit 1.0.0`):
  - Add: `Please see the [CHANGELOG](CHANGELOG.md) for further details.`
  - Upload the release package
- Close the release issue
- Close the milestone

## Key Points

- Use an established release number scheme to mark your software releases.
- Make sure that all relevant information is contained in the release package.
- Keep a user-readable changelog.
- Establish a clear and well-automated process for release creation.
