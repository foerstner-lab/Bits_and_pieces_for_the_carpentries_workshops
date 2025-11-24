<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 6 - Perform Iteration 3

- Objective: Learn how to apply the exemplary change process in practice
- Estimated time: 120min
- Teaching techniques: Interactive Exercise

## Explain the Goals of Iteration 3

- Finalize release 1.0.0:
  - Add missing calculations (at least: average, variance, standard deviation)
  - Add support for reading sample values from files
  - Add logging support

## Explain the current Iteration Status

- Two additional tasks have been already performed:
  - Review process via merge requests has been established
  - Release process has been finalized (more later)
- We are responsible for implementing the missing features.

## Explain the foreseen Change Process

- Focus on the review process including review checklist and required approval:

```
Create issue =>
Create merge request => 
Clone Git repository and switch to branch =>
Perform tasks =>
Commit and push changes =>
Review changes =>
Merge changes
```

> Please see [Introduction to Reviews](../../02_git-and-gitlab-for-teams/episodes/episode06.md#introduction-to-reviews) for details about code reviews.

## Initiate the Implementation Phase

- Determine teams (2 participants form 1 team):
  - Up to 9 teams to [implement the missing calculations](../code/04_team-exercise/task-calculations)
  - 1 team to [implement the file input method](../code/04_team-exercise/task-file-input)
  - 1 team to [implement logging](../code/04_team-exercise/task-logging)
- Explain to every team the details of their tasks
- Officially start the implementation phase

## During the Implementation Phase

- Give support and answer questions
- Make sure that no team falls too far behind

## Close the Implementation Phase

- Perform the review meeting:
  - Check the latest build pipeline
  - Download the latest snapshot release
  - Install it locally and test it

## Key Points

- A typical iteration consists of a planning, implementation, and review phase.
- A clear and well automated change process is important to avoid code quality issues.
- The combination of issues, merge requests, and pipelines allow the implementation of efficient change processes.
- Code reviews can be embedded in a lightweight way and improve code quality as well as knowledge sharing in the team.
