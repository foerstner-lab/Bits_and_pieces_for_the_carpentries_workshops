<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 1 - Introduction and Quiz

- Objective: Introduction and Recap of Git basics
- Estimated time: 30min
- Teaching techniques: Interactive Exercise

## Introduction

- Introduce the objectives for this session
- Explain how the live coding will be carried out

## Exercise 1

1. Git is a centralized VCS
2. Git is a decentralized VCS

<details>
<summary>Solution:</summary>

- See [git-scm.com: About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

</details>


## Exercise 2

Explain the purpose of the following command `git init`.
<details>
<summary>Solution:</summary>

`git init` initializes a new repository within the folder the command is issued in. 

</details>


What is the `.git` folder used for?
<details>
<summary>Solution:</summary>

The `.git` holds **all** information and configuration of the Git version control system.
</details>


## Exercise 3

Explain the following commands:

1. `git config -–global user.name "Vlad Dracula"`
2. `git config --global user.email "vlad@tran.sylvan.ia"`

<details>
<summary>Solution:</summary>

1. Sets the username used in commits
2. Sets the email used in commits

The `--global` options sets both to the whole Git installation.
Without this option the username and email is set to the git repository withon the command was issued.
</details>


## Exercise 4

Solve ["Choosing a Commit Message"](http://swcarpentry.github.io/git-novice/04-changes/index.html#choosing-a-commit-message) from Software Carpentries


## Exercise 5

Solve ["Commit Changes to Git"](http://swcarpentry.github.io/git-novice/04-changes/index.html#committing-changes-to-git) from Software Carpentries

See also [Modify-Add-Commit Workflow](http://swcarpentry.github.io/git-novice/fig/git-staging-area.svg)


## Exercise 6

How is `git diff` different from `git diff --staged`?
<details>
<summary>Solution:</summary>

With the option `--staged` the difference between the staging area and the last commit is shown.
Otherwise the difference between the working copy and the last commit is shown. 

</details>

## Exercise 7

Solve ["Recovering Older Versions of a File"](http://swcarpentry.github.io/git-novice/05-history/index.html#recovering-older-versions-of-a-file) from Software Carpentries


## Exercise 8

Solve ["Understanding Workflow and History"](http://swcarpentry.github.io/git-novice/05-history/index.html#understanding-workflow-and-history) from Software Carpentries


## Exercise 9

How is `git push` different from `git commit`?
<details>
<summary>Solution:</summary>

`git push` pushes commits to another repository.

`git commit` creates a new commit in the local repository.

In contrast to `svn commit`, `git commit` is a local operation and does not require a server.
</details>


## Exercise 10

How is `git pull` different from `git fetch`?
<details>
<summary>Solution:</summary>

`git pull` updates the local meta information of another repository and directly pulls change sets/commits.

`git fetch` only updates the local meta information of another repository.
</details>

How is `git pull` different from `git checkout`?
<details>
<summary>Solution:</summary>
    
`git pull` updates the local meta information of another repository and directly pulls change sets/commits.

`git checkout` replaces the current version of a local file with another version. This is a local operation.
</details>


## Exercise 11 

What is `git switch` used for?
<details>
<summary>Solution:</summary>
    
Replaces `git checkout <branch>` in Git version >= 2.23
</details>


What is `git restore` used for?
<details>
<summary>Solution:</summary>
    
Replaces `git checkout -- <file>` in Git version >= 2.23
</details>


## Key Points

- We recapped the Git basics which we need to start with the exercises.
