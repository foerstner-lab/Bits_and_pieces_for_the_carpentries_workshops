<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 8 - Bugfix Releases using Release Branches and Tags

- Objective: Understand how to manage bugfix releases using Git branches and tags
- Estimated time: 45min
- Teaching techniques: Live Demonstration

## Preparation

- **Problem:** We want to deliver bugfixes but no new features!
- There are different approaches to releasing / release branches:
  - The blog post gives an overview: https://medium.com/@patrickporto/4-branching-workflows-for-git-30d0aaee7bf
  - GitHub Flow / GitLab Flow: more CI/ CD centered => deployment branches
  - Git Flow / One Flow: more traditional approach => short-lived release / hot fix branches
- **What we use:**
  - We follow [One Flow](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow) as it is less complicated and its restrictions/assumptions are far better described.
  - Please see [Patterns for Managing Source Code Branches](https://martinfowler.com/articles/branching-patterns.html) (Release Branch, Hotfix Branch) for further reference.
- Make sure you still have the alias `git graph` defined: `git config --global alias.graph "log --all --decorate --oneline --graph"`
- Create a new GitLab project named `bugfix-releases`
- Add a `README.md` file with the following content (`GitLab => Add README`):

```
# Perform Bugyfix Release with Git Tags and Branches

- Some content...

```

- Tag the release `0.1.0` (`Repository => Tags`, no notes)
- Clone the repository: `git clone <Git Repository URL>`

## Create Bugfix Release 0.1.1 - No conflicting Changes on master

- Create the release branch for the bugfix: `git checkout -b release/0.1.1 0.1.0` (Git version >= 2.23 supports: `git switch -c <BRANCH NAME>`)
- Fix typo in the caption and commit the change to release branch:
  - `git add README.md`
  - `git commit -m "Fix caption typo"`
- Tag the bugfix release: `git tag 0.1.1`
- Add more content to the `README.md` on the `master` branch via GitLab
- Switch to the master and pull it:
  - `git checkout master` (Git version >= 2.23 supports: `git switch <BRANCH NAME>`)
  - `git pull origin master`
- Merge the release branch: `git merge release/0.1.1`
- Show the result: `git graph`
- Push the master including the tag: `git push --tags origin master`
- Delete local release branch: `git branch -d release/0.1.1`
- Show result in GitLab:
  - `master` => Typo fix + new content
  - `0.1.1` release tag => Typo fix only

## Create Bugfix Release 0.1.2 - Conflicting Changes on master

- Add the release number to the caption of the `README.md` file on the `master` branch via GitLab

```
# Perform Bugfix Release with Git Tags and Branches (version: 0.2.X)
```

- **Problem:** The release number should be also available for releases 0.1.X
- Create the release branch for the bugfix: `git checkout -b release/0.1.2 0.1.1` (Git version >= 2.23 supports: `git switch -c <BRANCH NAME>`)
- Add the release number to the caption of the `README.md` file:
  - Add `(version: 0.1.X)`
  - `git add README.md`
  - `git commit -m "Add version tag"`
- Tag the bugfix release: `git tag 0.1.2`
- Switch to the master and pull it:
  - `git checkout master` (Git version >= 2.23 supports: `git switch <BRANCH NAME>`)
  - `git pull origin master`
- Merge the release branch: `git merge release/0.1.2`
- Resolve the conflict:
  - Use `master` branch version
  - `git add README.md`
  - `git commit`
- Show the result: `git graph`
- Push the master including the tag: `git push --tags origin master`
- Delete the local release branch: `git branch -d release/0.1.2`
- Show result in GitLab:
  - `master` => Nothing changed
  - `0.1.2` => Version tag without other content
  - Show `Repository => Graph`, explain branches to sum it up

## Key Points

- The demonstrated approach allows you deliver bugfixes without new features and to properly track all changes on the (long-lived) `master` branch.
- Please make sure to clean up short-lived branches immediately but **do not forget to push your release tags to master**!
- The usage of short-lived release branches and tags is a more traditional approach.
  Please consider the alternatives to make sure that you use an approach fitting your actual needs.
