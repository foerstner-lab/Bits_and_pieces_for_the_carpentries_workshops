<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 2 - Set up the Issue Tracker

- Objective: Understand how to set up and use the GitLab issue tracker
- Estimated time: 60min
- Teaching techniques: Live Demonstration

## Preparation

- Show the base GitLab project
- Create a new issue via `Issues=>New Issue`

```
Name: Set up the issue tracker

Description:

## What is the purpose of the change?

- Make sure that we have an issue tracker basically configured to ease planning and work

## Which tasks have to be performed?

- [ ] Set up labels
- [ ] Set up milestones
- [ ] Set up issue templates

Assignee: Yourself
```

## Setup of the Labels

- Labels help to categorize and find issues.
- Set up the labels including their description in `Issues=>Labels`:
  - `type::feature`, color: blue, description: Marks new features
  - `type::bug`, color: orange, description: Marks errors
  - `type::enhancement`, color: blue, description: Marks improvements
  - `type::release`, color: blue, description: Marks release preparations
  - `component::calculation`, color: green, description: Marks tasks related to calculations
  - `component::inputs`, color: green, description: Marks tasks related to input methods

- Prioritize bug, release
- `::` is for issue scoping to ease label categorization
- Check task 1 (label setup) in the created issue
- Add label `type::enhancement` to the issue

## Setup of the Milestones

- Milestone ease planning of related tasks that have to be finished at the same time.
- Create milestone for this iteration via `Issues=>Milestones=>New Milestone`

```
Name: Release 0.2.0

Description: Capture results of iteration 2
```

- Create next milestone

```
Name: Release 1.0.0

Description: Capture results of the initial release
```

- Assign created issue to the first milestone (Iteration 2)
- Check task 2 (milestone setup)
- Set milestone to `Release 0.2.0`

## Add the Issue Templates

### Preparation

- Issue templates help to provide default texts for the issue description.
  For example, it is important to have sufficient information to reproduce a bug.
  In this case, the template can already provide a dedicated section for this information.
  Such a hint in the description helps the issue reporter to correctly provide this information.
- Make sure everyone has the [prepared templates](../code/02_issue-templates) on their local disk
- Clone the Git repository of the forked GitLab project

### Add the Templates to the Repository

- Create a merge request from the issue
- Pull the new branch into the local Git repository
- Copy the templates files and add them to the repository
- Commit them (`git commit -m "Add issue templates"`)
- Push them to the remote feature branch (`git push`)
- Switch to the merge request and repeat basic merge request concepts (focus: issue closing)
- Merge the merge request into the `master` branch
- Show that the issue has been closed automatically but check task 3 (issue template setup) as well

### Demonstrate the Usage of Issue Templates

- Create a new issue
- Show the different templates (explain purpose and specifics such as quick actions) 

## Key Points

- The GitLab issue tracker allows us to get easily started.
- But it provides many powerful features such as labels, milestone planning, templates, integration with other GitLab tools.
- Common setup steps include the definition of labels, milestones, and issue description templates.
