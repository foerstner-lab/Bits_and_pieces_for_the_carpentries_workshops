<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 6 - Basic Collaboration using GitLab

- Objective: Show basic workflows such as branching and merging within GitLab
- Estimated time: 45min
- Teaching techniques: Live Demonstration

## Add Collaborators in GitLab

This section requires the participants to team-up in pairs of two.

- One participant has the role `Owner`, the other one has the role `Contributor`
- Show options for merge requests
  - Enable `Approval are needed`
  - Enable `All discussions must be resolved`
- Show how the `Owner` can invite a new `Contributor` to the GitLab project


## Prepare the Merge Request (Contributor view)

Here the `Contributor` prepares some work.

- Create a new branch via the GitLab UI
  - Name it: `add-new-author`
- Clone the repository of your teammate via: `git clone <repo url>`
- Update the local Git repository via: `git fetch -v`
- Switch to branch `add-new-author`
  - `git checkout -b add-new-author` (Git version >= 2.23 supports: `git switch <BRANCH NAME>`)
  - Highlight that Git automatically connects the remote branch
  - Verify it `git pull origin add-new-author`
  - Highlight that we are already on the latest commit
- Show current state of the local Git repository via: `git graph`
- Add yourself to the `CONTRIBUTORS.md` (see also: [CONTRIBUTORS.md](../code/06_collaboration_step-1/CONTRIBUTORS.md))
  - `git add CONTRIBUTORS.md`
  - `git commit -m "Add myself as contributor"`
- Show current state of the repository via: `git graph`
- Push new branch to the remote repository via: `git push origin add-new-author`


## GitLab Merge Requests

### Merge Request on the original GitLab Project

Here the `Contributor` creates a merge request for the `Owner`.

- Show how a merge request is created
  - Add a **good** title: `Add repository documentation`
  - Explain what can be put into the description (e.g. checklists for contributors and reviewers)
  - Mention that merge requests can be created from issues (next day)
  - Explain the `delete branch` and `squash` options
  - Highlight that merge requests simplify the local steps
  - **Please note:** The merge request will be created in the original (forked) GitLab project.
- Show what happened on the original repository
  - A lot of merge requests have been created
- Explain `Open`, `Closed`, `Merged` state of merge requests 
  - Let the `Contributors` close the merge request


### Create a Merge Request to the Owner's GitLab Project

Show how to manually change the GitLab project the merge request is created against.

### Introduction to Reviews

#### General Considerations

- `Contributor`: 
  - Use automated formatter to keep diffs small
  - Use spell-checker, linter, etc. 
  - Include both code and automated tests in one merge request
  - Annotate code about which you want specific feedback
  - `@mention` the right people
- `Reviewer` (here: `Owner`):
  - It is about the code, its improvement, and understanding it as a team
  - Start with a summary and positive feedback
  - Use "we" instead of "you"
  - Criticize ideas, structure or important features of the code but **NOT** its author or minor details
- Ask questions rather than making statements
- Say "Thank you"
__
#### Process in GitLab

- Explain merge review
  - Show that lines can be annotated
  - Show option of the editor.
  - Add comment: `Normally, contributors are added to the file by the owner, after they really contributed something.`
- Let the `Contributor` respond to it.
- Let the discussion be resolved by the `Owner`
  - Explain options, `new issue` and `direct resolve`
  - Show that we can change how strict GitLab behaves
- Approve the merge request
  - The `Owner` approves the merge request
- The `Contributor` merges the merge request

## Key Points

- GitLab simplifies some tasks, normally done in the command line interface.
- GitLab allows to create a merge requests from a branch.
- GitLab tracks all changes within the merge requests.
- GitLab enables interactive reviews for merge requests.
- Reviews are about the code, its improvement, and understanding it as a team.
