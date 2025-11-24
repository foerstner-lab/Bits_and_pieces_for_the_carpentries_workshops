<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 3 - Branching and Merging

- Objective: Learn basic branching and merging techniques
- Estimated time: 60min
- Teaching techniques: Live Coding

## Introduction

We extend the initial sample calculator prototype to learn some basic branching concepts in Git.

### Background

- Branches are an important concept in Git.
- They are much more integrated in daily work than in SVN.
- Every Git repository can contain as many branches as you want.
- Every Git repository can have different branches.
- Branches can be shared between Git repositories.

## Basic Branching (step 1)

We explore the repository, create our initial feature branches, and do some work on them.

### Explore the Repository

- Change to the directory `sample-calculator-iteration-1`
- Show the existing branches
  - `git branch --all`
  - Explain the labels `master` and `HEAD`
  - Explain remote and local branches
- Show graph of the repository
  - Draw state of the repository
  - Verify with `git graph`

```
o - o <- HEAD, master
```

### Create initial Branches

- Create two new branches
  - `git branch add-usage-hint`
  - `git branch feature-2`
- Show what changed
  - `git branch`
  - Explain that `*` marks where the HEAD is pointing to

### Rename a Branch

- Rename branch `feature-2` to `add-contributor-guide`
  - `git branch -m feature-2 add-contributor-guide`
  - Verify with `git branch`
  - Explain what happened and verify it with `git graph`

```
o - o <- HEAD, master, add-usage-hint, add-contributor-guide
```

### Work on the first Branch

- Switch to branch `add-usage-hint`
  - `git checkout add-usage-hint` (Git version >= 2.23 supports: `git switch <BRANCH NAME>`)
  - Verify with `git graph`
- Add some new content
  - Add [README.md](../code/03_branch_and_merge_step-1/README.md) from workshop materials (step 1)
  - `git add README.md`
  - `git commit -m "Add information about how to use the software"`
- Show changes in the Git repository via: `git graph`

```
      o <- HEAD, add-usage-hint
     /
o - o <- master, add-contributor-guide
```

### Parallel Work on the second Branch

- Switch to branch `add-contributor-guide`
  - `git checkout add-contributor-guide` (Git version >= 2.23 supports: `git switch <BRANCH NAME>`)
  - Show that we moved the `HEAD` via: `git branch` and `git graph`
- Add some content
  - Update content of [CONTRIBUTING.md](../code/03_branch_and_merge_step-1/CONTRIBUTING.md) from workshop materials (step 1)
  - `git add CONTRIBUTING.md`
  - `git commit -m "Add contribution guidelines"`
- Show changes in the Git repository with `git graph`

```
      o <- add-usage-hint
     /
o - o <- master
     \
      o <- HEAD, add-contributor-guide
```

## Remote Branches (step 2)

Now, we push the last changes to the GitLab project.

### Pushing a new Branch

- Explain that we will push or latest branch to a remote repository (the GitLab Server)
  - Explain a GitLab server in the context of a Git repository 
  - Explain with graphics from [git-scm.com: About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- `git push origin add-contributor-guide`
- Show and explain where the branch can be found within the GitLab UI


### Perform Changes on the Remote Repository Branch

- Add yourself to the `CONTRIBUTORS.md` file as an contributor via the GitLab UI (see also: [CONTRIBUTORS.md](../code/03_branch_and_merge_step-2/CONTRIBUTORS.md))
- Use `Add myself as contributor` for the commit message

### Retrieve Changes from a Branch of a Remote Git Repository

- Explore what has changed on the remote via: `git fetch -v`
- Pull changes from the branch via: `git pull origin add-contributor-guide`
- Explore how the local repository has changed via: `git graph`

```
      o <- add-usage-hint
     /
o - o <- master
     \
      o - o <- HEAD, add-contributor-guide
```

## Basic Merging Techniques

Now, we want to merge the previous work from the feature branches into the `master` branch.

### A simple Fast-Forward-Merge

- Switch to `master` branch via: `git checkout master` (Git version >= 2.23 supports: `git switch <BRANCH NAME>`)
- Show difference between the branches `master` and `add-usage-hint` via: `git diff master..add-usage-hint`
- Merge the `add-usage-hint` branch into the `master` branch
  - `git merge add-usage-hint master`
  - Merge executed as Fast-Forward-Merge
- Explain Fast-Forward-Merge and why it is possible
  - Fast-Forward-Merge means the branch label of `master` is moved to `add-usage-hint`
  - Both share the same history, i.e., the `master` label position is only updated
- Verify with `git graph`

```
o - o - o <- HEAD, master, add-usage-hint
     \
      o - o <- add-contributor-guide
```

### Clean up

- Show how you can check that branches are merged
  - `git branch --merge`
  - Only branches that merged branches are listed
  - The branch we are on is the base
- Delete branch `add-usage-hint`, since it is merged, via: `git branch -d add-usage-hint`
- Show that we **cannot** delete the other branch with the command yet:
  - `git branch -d add-contributor-guide`
  - Explain that we can do this with the `-D` option but we would lose our work


### A simple 3-Way-Merge

- Merge the branch `add-contributor-guide` into the branch `master`
  - `git merge add-contributor-guide`
  - Highlight that the merge was performed by using the recursive strategy
  - This merge type is called `Non-Fast-Forward-Merge` or `3-Way-Merge`
  - Explain that Fast-Forward-Merge is not possible, since there is no direct chained history
- Verify with `git graph`

```
o - o - o - o <- HEAD, master, add-contributor-guide
     \     /
      o - o 
```

### Final clean up

- Delete branch `add-contributor-guide`, since it is merged, via: `git branch -d add-contributor-guide`
- Delete the remote branch in the GitLab project via: `git push origin --delete add-contributor-guide`

## Pros and Cons of a 3-Way-Merge

| Pros | Cons |
| ------ | ------ |
| Simple and familiar | Bulky, if long living branches are the norm |
| Preserves complete history | Non-linear history in main branch |
| Preserves chronological order | Merge commits in main branch |
| Maintains context of the branch | |

## Key Points

- A Git repository can have multiple branches at the same time.
- New branches can be created at any time on any branch.
- Branches can be used to organize work.
- Branches can be pushed to other repositories.
- Branches can be pulled from other repositories.
- You can use `Fast-Forward-Merge` or `3-Way-Merge` to integrate your work into the `master`.
