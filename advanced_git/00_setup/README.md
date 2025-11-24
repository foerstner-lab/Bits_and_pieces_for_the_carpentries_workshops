<!--
SPDX-FileCopyrightText: 2021 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Workshop Setup

Here you find basic information about the workshop setup.

## Plan the Schedule

We use the following schedule for an online setup of the workshop.
Smaller breaks are not included but we try to have a 15 minutes break every 90 minutes.

### Day 1

- 09:00 - 09:30 Welcome & Introduction
- 09:30 - 11:00 Introduction to Software Processes and Change Management
- 11:00 - 12:00 Git for Teams - Introduction and Quiz, Preparation
- *12:00 - 13:00 Lunch Break*
- 13:00 - 14:50 Git for Teams - Branching and Merging, Rebasing
- 14:50 - 15:00 Wrap Up & Feedback Day 1

### Day 2

- 09:00 - 09:10 Welcome & Introduction
- 09:10 - 10:30 Git for Teams - Rebasing (Cont.), Conflicts
- 10:30 - 12:00 Example Project - Introduction, Issue Tracking
- *12:00 - 13:00 Lunch Break*
- 13:00 - 14:30 Example Project - Build Pipeline
- 14:30 - 14:50 Example Project - Close Iteration 2
- 14:50 - 15:00 Wrap Up & Feedback Day 2

### Day 3

- 09:00 - 09:10 Welcome & Introduction
- 09:10 - 11:30 Team Exercise
- 11:30 - 12:00 Release Version 1.0.0
- 12:00 - 12:45 Reflecting your own Development Workflow
- 12:45 - 13:00 Wrap Up & Feedback

## Set up the Code Examples

The code examples are used for interactive exercises and live demonstrations.

- [ ] Create a GitLab group for the example projects: Name: `YYYY-MM-DD GitLab for Software Development in Teams`, Description: `This group contains the materials and code examples used in the workshop.`, Logo: [group-logo.jpg](images/group-logo.jpg)
- [ ] Create the following **empty** GitLab projects within the group:
  - Name: `Example Project - Iteration 1`, Description: `Status of Sample Calculator at the beginning of the first iteration.`, Logo: [iteration1-logo.png](images/iteration1-logo.png)
  - Name: `Example Project - Iteration 2`, Description: `Status of Sample Calculator in the middle of the second iteration.`, Logo: [iteration2-logo.png](images/iteration2-logo.png)
  - Name: `Example Project - Iteration 3`, Description: `Status of Sample Calculator at the beginning of the third iteration.`, Logo: [iteration3-logo.png](images/iteration3-logo.png)
- [ ] Initialize the Git repositories of the GitLab projects:
  - Configure the Git URL and run [init-git-example1.sh](scripts/init-git-example1.sh) to initialize `Example Project - Iteration 1`.
  - Configure the Git URL and run [init-git-example2.sh](scripts/init-git-example2.sh) to initialize `Example Project - Iteration 2`.
  - Configure the Git URL and run [init-git-example3.sh](scripts/init-git-example3.sh) to initialize `Example Project - Iteration 3`.
- [ ] Fine tune the configuration of the GitLab projects:
  - `Example Project - Iteration 1`:
    - Make sure to only activate the GitLab features: `Repository`, `Merge requests`, `Forks`.
  - `Example Project - Iteration 2`:
    - Make sure to only activate the GitLab features: `Repository`, `Merge requests`, `Forks`, `Issues`, `Pages`.
  - `Example Project - Iteration 3`:
    - Make sure to only activate the GitLab features: `Repository`, `Merge requests`, `Forks`, `Issues`, `Pages`, `Pipelines`.
    - Configure a GitLab runner which supports docker usage and defines the tag `docker`.
    - Start a build pipeline for the main branch and check that it runs successfully.
    - Configure and run [prepare-example3.py](scripts/prepare-example3.py) to initialize labels, milestones, issues, and badges.
      Do not forget to provide an appropriate `gitlab-config.ini` with a *gitlab4teams* entry.
      Please see the script for further setup information.
      Please beware that some badge images (pipeline, coverage) are only available after an initial successful pipeline run.
      
## Setup the Pad

The directory [pads](pads) contains pad templates that we usually set up in a service such as [HedgeDoc](https://hedgedoc.org/):
- Throughout the whole workshop, we use the [Main Pad](./setup/pads/main.md).
- Please copy and modify the pad to your needs
- Content to be changed is indicated by `[setup]`

