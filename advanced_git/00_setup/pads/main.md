<!--
SPDX-FileCopyrightText: 2021 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

<!--
This markdown file is a template for your markdown-pad. Please copy and modify the pad. Content to be changed in the source is indicated by [setup].
-->

[setup]: # (add workshop date)

# GitLab for Software Development in Teams (DD.-DD.MM.YYYY)

## Open Questions



## Agenda

[setup]: # (possible schedule; please modify date and times according to your needs)

### Day 1 - DD.MM.YYYY
- 09:00 - 09:30 Welcome & Introduction
- 09:30 - 11:00 Introduction to Software Processes and Change Management
- 11:00 - 12:00 Git for Teams - Introduction and Quiz, Preparation
- *12:00 - 13:00 Lunch Break*
- 13:00 - 14:50 Git for Teams - Branching and Merging, Rebasing
- 14:50 - 15:00 Wrap Up & Feedback Day 1

> We try to have a 15 minutes break every 90 minutes.


### Day 2 - DD.MM.YYYY
- 09:00 - 09:10 Welcome & Introduction
- 09:10 - 10:30 Git for Teams - Rebasing (Cont.), Conflicts
- 10:30 - 12:00 Example Project - Introduction, Issue Tracking
- *12:00 - 13:00 Lunch Break*
- 13:00 - 14:30 Example Project - Build Pipeline
- 14:30 - 14:50 Example Project - Close Iteration 2
- 14:50 - 15:00 Wrap Up & Feedback Day 2

> We try to have a 15 minutes break every 90 minutes.

### Day 3 - DD.MM.YYYY
- 09:00 - 09:10 Welcome & Introduction
- 09:10 - 11:30 Team Exercise
- 11:30 - 12:00 Release Version 1.0.0
- 12:00 - 12:45 Reflecting your own Development Workflow
- 12:45 - 13:00 Wrap Up & Feedback

> We try to have a 15 minutes break every 90 minutes.

## Organizational Details


### Before the Workshop
- [ ] You need a computer equipped with
	- a simple text editor (e.g. Notepad ++, gedit, ...)
	- a recent [Chromium based browser](https://en.wikipedia.org/wiki/Chromium_%28web_browser%29#Active) (e.g., Chromium, Microsoft Edge)
	- and the Git command-line tool.
- [ ] Please also check that you have an account and can log in to the [DLR GitLab](https://gitlab.dlr.de/).

[setup]: # ("please add a link to your preferred video conferencing tool. Also feel free to add system requirements and further links \(e.g. setup guide, FAQs, troubleshooting,...\) )

- [ ] Please connect to ...
    - Please **use a recent Chromium-based browser** (e.g., Chromium, Microsoft Edge). Other modern browsers (e.g. FireFox) might work as well but we noticed sometimes performance issues.
    - Please avoid using VPN (if you use any) to improve your connection performance.
    - For further information, please see:

### During the Workshop
- Please mute yourself if you are not talking.
- Please use a headset.
- Please be back in time after breaks / practice phases.
- Please ask your questions in the chat during the presentation.


[setup]: # (insert link to example code; group name is the date of first day of the workshop)

## Important Links
- [Workshop materials](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials) 
- [Example codes](https://gitlab.dlr.de/ws-sd-for-teams/YYYY-MM-DD)


[setup]: # (add workshop date)

# Day 1 - DD-MM-YYYY
## Welcome & Introduction
- Please tell us in a minute about your background and interest in research software.
- You can switch on your camera, if you like :)


## Introduction to Software Processes & Change
- [Episode 01 - "Introduction"](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/01_introduction/README.md)


## Exercise - What about your Development Process? (45min)

Please think about a concrete software that you develop (alone or with others):
1. Please describe the context (e.g., how many developers, their availability, etc.).
2. Please visualize the change process:
    - Which steps are performed to get a change into a usable software version 
    - Which tools and practices do you use?
    - Are there any automatic checks / reviews / feedback steps involved?
3. Which aspects of the change process work well and which of them could require improvements?
 

[setup]: # (add more Breakout Rooms if needed)

### Breakout Room 1

### Breakout Room 2



## Git for Teams - Summary and Quiz
- [Episode 01 - Summary and Quiz](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/02_git-for-teams/episodes/episode01.md)


### Exercise 1
1. Git is a centralized VCS
1. Git is a decentralized VCS

#### Solution
2
[https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)


### Exercise 2
Explain the purpose of the following command `git init`.

What is the `.git` folder used for?

#### Solution
The .git holds all information and configuration of the Git  
&#10;version control system.


### Exercise 3
Explain the following commands:
1. `git config -–global user.name “Vlad Dracula”`
1. `git config --global user.email “vlad@tran.sylvan.ia”`


#### Solution
1. Sets the username used in commits
1. Sets the email used in commits

The `--global` options sets both to the whole Git installation.  
&#10;Without this option the username and email is set to the git repository withon the command was issued.


### Exercise 4
Solve [“Choosing a Commit Message”](http://swcarpentry.github.io/git-novice/04-changes/index.html#choosing-a-commit-message) from Software Carpentries


### Exercise 5
Solve [“Commit Changes to Git”](http://swcarpentry.github.io/git-novice/04-changes/index.html#committing-changes-to-git) from Software Carpentries

See also [Modify-Add-Commit Workflow](http://swcarpentry.github.io/git-novice/fig/git-staging-area.svg)

### Exercise 6
How is `git diff` different from `git diff --staged`?

#### Solution
With the option `--staged` the difference between the staging area and the last commit is shown.  
&#10;Otherwise the difference between the working copy and the last commit is shown.

### Exercise 7
Solve [“Recovering Older Versions of a File”](http://swcarpentry.github.io/git-novice/05-history/index.html#recovering-older-versions-of-a-file) from Software Carpentries

### Exercise 8
Solve [“Understanding Workflow and History”](http://swcarpentry.github.io/git-novice/05-history/index.html#understanding-workflow-and-history) from Software Carpentries

`git status` helps to see if there are changes is in the working directory or staging area and should be performed before commits and especially checkouts!

### Exercise 9
How is `git push` different from `git commit`?

#### Solution
`git push` pushes commits to another repository.

`git commit` creates a new commit in the local repository.

In contrast to `svn commit`, `git commit` is a local operation and does not require a server.

### Exercise 10a
How is `git pull` different from `git fetch`?

#### Solution
`git pull` updates the local meta information of another repository and directly pulls change sets/commits.

`git fetch` only updates the local meta information of another repository.

### Exercise 10b
How is `git pull` different from `git checkout`?

#### Solution
`git pull` updates the local meta information of another repository and directly pulls change sets/commits.

`git checkout` replaces the current version of a local file with another version. This is a local operation.

### Exercise 11a
What is `git switch` used for?

#### Solution
Replaces `git checkout <branch>` in Git version >= 2.23

### Exercise 11b
What is `git restore` used for?

#### Solution
Replaces `git checkout -- <file>` in Git version >= 2.23



## Git for Teams - Preparation for Live Coding

- [Episode materials](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/02_git-for-teams/episodes/episode02.md) 
- [Workshop materials](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials)

[setup]: # (change link to gitlab-group; group name is the date of first day of the workshop)

- [GitLab group](https://gitlab.dlr.de/ws-sd-for-teams/YYYY-MM-DD) in which we work during this workshop: 

### Prepare your Git Client environment
- Open Git Bash via right-click "Open Git Bash here"
- `mkdir git-and-gitlab-for-teams`
- `cd git-and-gitlab-for-teams`

### Check Settings
`git config --global user.name <your user name>`
`git config --global user.email <your email>`

### Create a Shortcut
`git config --global alias.graph "log --all --decorate --oneline --graph"`
 


### Clone the Workshop Materials Repository
`git clone https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials.git`


### Fork the Exercise Repository `Sample Calculator - Iteration 1`

[setup]: # (change link to gitlab-group)

- Open in your browser: https://gitlab.dlr.de/ws-sd-for-teams/YYYY-MM-DD/example-project-iteration-1
- Press the `Fork` button (upper right corner)
- Use your GitLab account as target for the fork
- Clone the forked repository: `git clone https://gitlab.com/<YOUR USERNAME>/example-project-iteration-1`

> **Forking** is copying the GitLab project (including its Git repository) into your private space or another space.

#### Authentication Failed
> If you get an error "Authentication failed", this might be due to Windows having saved an old password of you. Open "Anmeldeinformationsverwaltung" in Windows and switch to "Windows Credentials". Update your credentials there. You might have to do this everytime you change your password.
> Newer versions of Git for Windows present the authentication dialog again, if the first attempt failed.


## Git for Teams - Branching and Merging with Git
- [Episode materials](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/02_git-for-teams/episodes/episode03.md) 

### Introduction and Preparation
- We now have two projects in our folder `git-and-gitlab-for-teams`
- `cd example-project-iteration-1`
- `git remote -v` -> Check origin URL
- `git branch` -> one master branch
- `git branch --all` -> one master branch as well as remotes
- `git graph` => Shows one commit
- `git branch add-usage-hint` => Creates a branch
- `git branch` => Shows 2 (local) branches
- `git branch feature-2` => Creates a second branch
- `git branch` => Shows 3 (local) branches
- `git branch -m feature-2 add-contributor-guide` => Rename the second branch to show a better name
- `git branch` => Shows 3 (local) branches including the second branch with the new name


### Work on the First Branch
- `git switch add-usage-hint` => Switch to the first branch
- `git graph` => The `HEAD` is now pointer to `add-usage-hint`
- Copy `workshop-materials/02_git-for-teams/code/03_branch_and_merge_step-1/README.md` to your working copy
- `git status` => `README.md` has changed but not yet staged or committed
- `git add README.md`
- `git commit -m "Add information how to use the software"`
- `git graph` => Check the current status


### Work on the Second Branch
- `git switch add-contributor-guide`
- Copy `workshop-materials/02_git-for-teams/code/03_branch_and_merge_step-1/CONTRIBUTING.md` to your working copy
- `git add CONTRIBUTING.md`
- `git status` => A new file is read to commit
- `git commit -m "Add contribution guidelines"` => Commit it
- `git graph` => Check the current status

Result:

          o <- add-usage-hint
         /
    o - o <- master
         \
          o <- HEAD, add-contributor-guide


- Push the branch to the remote repository: `git push origin add-contributor-guide`
- `git graph` => Check the current status, now there is a remote branch for `add-contributor-guide` as well

### Merge add-usage-hint
- `git switch master` => Switch to master branch
- `git diff master..add-usage-hint` => Show differences between branch master and add-usage-hint
- `git merge add-usage-hint` => Results in a Fast-Forward-Merge
- `git graph` => HEAD label now on add-usage-hint branch
- `git branch --merge` => Shows which branches are on the same level as the current branch (current is marked) => Others are safe to remove
- `git branch -d add-usage-hint` => Removes the local branch (clean up)
- `git graph` => Label gone, but can be restored if necessary

### Merge add-contributor-guide
- `git merge add-contributor-guide` => Results in a Non-Fast-Forward-Merge
- `git graph` => HEAD commit now has two parents. All local branches on same level (only origin ones not)


## Git for Teams - Rebase
- Episode materials: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/02_git-for-teams/episodes/episode04.md

### Prepare the new work “Add changelog”
- `git branch add-changelog` => Create new branch for our new work
- `git switch add-changelog` => Switch to new branch
- Copy `workshop-materials/02_git-for-teams/code/04_rebase_step-1/CHANGELOG.md` to your working copy
- `git add CHANGELOG.md`
- `git commit -m “Add initial changelog”`
- Add the line `&gt; WARNING: Initial prototype which is not ready for productive use!` in section 0.1.0
- `git add CHANGELOG.md`
- `git commit -m “Add warning for release 0.1.0”`
- Verify with `git graph`



### Simulate ongoing work on master branch
- `git switch master`
- Copy `workshop-materials/02_git-for-teams/code/04_rebase_step-2/README.md` to your working copy
- `git add README.md`
- `git commit -m "Add usage hint for interactive mode"`
- Verify changes with `git graph` => No Fast-Forward Merge possible due to missing a direct line in the graph; you can use rebase if you want to avoid a merge commit


## Wrap Up and Feedback Day 1


[setup]: # (add workshop date)

# Day 2 - DD-MM-YYYY

## Introduction Day 2

### Rebase the Feature Branch (Continuing from yesterday)
- `git push` => Save the current master branch in the remote Git repository
- `git switch add-changelog`
- `git graph`
- `git rebase master` => The performed commits are now based on the latest commit on master => Fast-Forward Merge is possible again
> **CAUTION:** Do not use `rebase` on public branches because it changes the history record (changes commit IDs) which can cause a lot of trouble for others basing on the former history!
- `git switch master`
- `git merge add-changelog` => Now, it gets merge using a Fast-Forward Merge
- `git branch --merged` => Shows all already merged branches
- `git branch -d add-changelog` => Removes the local branch (clean up)


### Quiz

Fast Forward possible or not? See [graphs](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/02_git-for-teams/episodes/episode04.md#quiz) 


a) Yes
b) No
c) No
d) Yes

### Make your work public
- `git fetch` => Retrieve information about possible changes happening in the remote Git repository
- `git push origin master` => Publish all changes on GitLab


## Git for Teams - Conflicts
- Episode materials: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/02_git-for-teams/episodes/episode05.md

- `git checkout -b add-license-placeholder`
  Alternative for newer Git versions: `git switch -c add-license-placeholder`
- `cp ../workshop-materials/02_git-for-teams/code/05_conflicts_step-1/LICENSE.md .` => Add `LICENSE.md` file from workshop materials
- `git add LICENSE.md`
- `git commit -m "Add license template"`
- `git graph` => Verify changes


### Stash the current Work

- Add reference to `LICENSE.md` in the `README.md` at the bottom of the file:
```
## License

Please see the file [LICENSE.md](LICENSE.md) for further information about how the content is licensed.
```
- `git stash list` => Currently shows an empty list of stashed work
- `git diff` => Our changes are returned as expected
- `git stash` => Temporarily save the current work in the stash



### Fix something on `master` (step 2)
- `git checkout master` => Switch to master branch
- `cp ../workshop-materials/02_git-for-teams/code/05_conflicts_step-2/README.md .` => Copy the changed `README.md`
- `git add README.md`
- `git commit -m "Reference contribution guidelines and changelog"`


### Apply stashed Work on the Feature Branch
- `git switch add-license-placeholder`
- `git stash show stash@{0}` => Shows what was in the stash on position 0
- `git stash show COMMITID` => Alternative - just works with commitlike stashes, marked with ref/stash 
- `git stash list` => Show all stashed changes
- `git stash pop` => Retrieve and apply the stashed changes
- `git diff` => Our changes are now applied from the stack to the current branch
- `git add README.md`
- `git commit -m "Add license placeholder"`
- `git graph`
- `git stash list` => No more changes stashed



### Abort a Merge
- `git switch master`
- `git merge add-license-placeholder` => Conflict - Could not be fixed automatically. We have to fix it manually
- Git is aware of the merge and highlight merge status in the command line interface
- `git status` => Shows where the merge conflict is in unmerged paths - here just in `README.md`
- `git merge --abort` => Abort merge (i.e. if you currently don't know how to merge it)


### Merge by resolving the Conflicts
- `git merge add-license-placeholder` => Let's try again
- Open the `README.md`, look for the conflict markers (e.g., `<<<<<<<  ======= >>>>>>>`), and resolve the problem manually (here its only one conflict, but can be several in a file - then there are several markers)


- `git add README.md` => Indicate to git that you resolved the conflict
- `git status` => Shows that the merge is resolved and the files can be commited
- `git commit` => Conclude merge by committing the changes, merge message is created automatically including a summary for you (which is just a comment and does not end up in message)
- `git graph` => shows the typical 3-way-merge now
- `git show <MERGE COMMIT COMMIT ID >` => You can see what changed when resolving the conflict
- `git branch -d add-license-placeholder` => Clean up merged branch
- `git status` => Shows we are now ahead of `origin/master`
- `git push origin master`


## Example Project | Iteration 2: Explain the Project Context and our Tasks
- [Explain the Project Context and our Tasks](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/03_example-project/episodes/episode01.md)

## Example Project | Iteration 2: Set up the Issue Tracker (Live Demonstration)
- [Set up the Issue Tracker](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/03_example-project/episodes/episode02.md)


## Example Project | Iteration 2: Introduction to Build Automation
- [Introduction to Build Automation](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/03_example-project/episodes/episode03.md)
- It is definitely worth to automate the build process!
- But automation is no "silver bullet"!
  Please make sure that it's worth the time :) ![xkcd about automation](https://imgs.xkcd.com/comics/is_it_worth_the_time_2x.png)

## Example Project | Iteration 2: Set up the Build Pipeline

- [Set up the Build Pipeline](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/03_example-project/episodes/episode04.md)


### Basic Requirements
- Please make sure that you have automated your *build process* using a kind of build script (e.g., Makefile, Maven, shell script etc.)
- You require a [GitLab runner](https://docs.gitlab.com/ee/ci/runners/README.html) to execute your build script
- Either you can use a shared/group runner or you need to [set up your own runner](https://docs.gitlab.com/runner/)




### Overview of a Generic Build Pipeline
- A generic GitLab pipeline looks basically as follows:
![](https://pad.gwdg.de/uploads/upload_d7cd0eaf8b8f014d298b7dacaf80024e.png)
  - A pipeline is executed from left to right
  - The columns of the pipeline are called *stages*
  - Every build job of a stage must succeed to start the next stage
  - Build jobs are atomic, can run independently and normally share no common state. But you can use caching, artifacts and package registries to "connect" them
  - Tags are used to match build jobs with GitLab runners
  - In the workshop, we use pre-configured runner provided by GitLab Inc.

### Preparation

#### Fork the Exercise Repository `Sample Calculator - Iteration 2`

[setup]: # (change link to gitlab-group)

- Open in your browser: [https://gitlab.dlr.de/ws-sd-for-teams/YYYY-MM-DD/example-project-iteration-2](https://gitlab.dlr.de/ws-sd-for-teams/YYYY-MM-DD/example-project-iteration-2)
- Press the `Fork` button (upper right corner)
- Use your GitLab account as target for the fork

#### Remove the Fork Relation
- Open in your browser your forked GitLab project and open the `Settings`
- Select `Settings`, scroll down to the `Advanced` section and click the `Expand` button
- Scroll down and select the `Remove fork relationship` button
- Confirm the removal of the fork relationship

#### Start your Work by defining the Task
- Switch to the project overview page of your forked GitLab project
- Create an issue as follows:
```
Name: Set up the build pipeline

Description:

## What is the purpose of the change?

- Make sure that the build script checks have been performed before new
  changes are introduced on the `master` branch.

## Which tasks have to be performed?

- [ ] Set up build runner
- [ ] Set up basic build pipeline
- [ ] Add badges to make results easier accessible

## Are there any acceptance criteria to check?

- [ ] Check everything via the merge request for this change

Assignee: Yourself
```

### Set up the Build Runner

- Activate the build pipeline in `Settings=>General=>Visibility, project features, permissions=>Pipelines`
- Switch to `Settings=>CI / CD=>Runners` to configure / select a specific runner:
  - Here we use an available shared runner provided by GitLab Inc.
  - Runner labels are used to match build jobs and runner. We need a runner which has a `docker` label.
  - Depending on your GitLab instance ask the administrators or your IT department for help
- Switch to your created issue and check the corresponding task


### Set up the Basic Build Pipeline
- Create a merge request from the issue: Selcet the `Create Merge Request` button


#### Create a First Test Build Job
- Create a new file via the `Create file` button
- Name the file `.gitlab-ci.yml`
- **Alterantive:** Switch to `CI/CD => Editor`, select the right branch, Select `Create new CI/CD pipeline`

- Add the following content:
```
test:
  image: python:3.6
  stage: test
  script:
    - pip install poetry
    - poetry install
    - make test
  tags:
    - docker
```
- You can check the pipeline script with the CI linter
- Commit changes with the message: `Add initial test job`
- See the running pipeline in `CI / CD => Pipelines`, select latest pipeline (separate tab)


#### Make the Test Report available
- Edit the file `.gitlab-ci.yml` and make the test report available in the merge request:
```
test:
  image: python:3.6
  stage: test
  script:
    - pip install poetry
    - poetry install
    - make test
  tags:
    - docker
  artifacts:
    reports:
      junit: build/tests.xml
```
- Commit changes with the message: `Make the test report available`
- See the details of our merge request (separate tab) and refresh the Web page if necessary.
  You are now able to the detailed test results.




#### Perform additional Code Checking (not shown in the workshop)
- Edit the file `.gitlab-ci.yml` and add an audit build job:
```
stages:
  - test
  - audit

# Definition of the test build job...

audit:
  image: python:3.6
  stage: audit
  script:
    - pip install poetry
    - poetry install
    - make audit
  coverage: '/^TOTAL.+?(\d+\%)$/'
  tags:
    - docker
  artifacts:
    expose_as: "Coverage Report"
    paths: ["build/htmlcov/"]
```
- Commit changes with the message: `Add an audit build job for extended code checking`
- See the running pipeline in `CI / CD => Pipelines`, select latest pipeline (separate tab)

- Let us fix the failing license information check by editing the file `.gitlab-ci.yml`:
```
# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT

# Other pipeline code as is ...
```
- Commit changes with the message: `Add missing license information`
- See the details of our merge request (separate tab) and refresh the Web page if necessary.
  The pipeline ran successfully. In addition, you can see the coverage report.
 
- [Configuration of the badges](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/03_example-project/episodes/episode04.md#add-badges-to-make-results-easier-accessible)

## Wrap up and Feedback Day 2

[setup]: # (add workshop date)

# Day 3 - DD-MM-YYYY

## Introduction and Welcome

## Example Project | Iteration 2: Close Iteration 2 (Live Demonstration)
- [Close Iteration 2](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/03_example-project/episodes/episode05.md)

## Example Project | Iteration 3: Perform Iteration 3 (Team Exercise)
- [Perform Iteration 3](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/03_example-project/episodes/episode06.md)

- [Reviews](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/02_git-for-teams/episodes/episode06.md)

### Step 0: What do you need?

[setup]: # (change link to gitlab-group)

- [Team GitLab project](https://gitlab.dlr.de/ws-sd-for-teams/YYYY-MM-DD/example-project-iteration-3)
- [Task descriptions](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise)
- [The cloned workshop materials repository](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials.git)

### Step 1: Determine the Teams

> If there are any problems write in the main room chat!
> You have normally time until you are finished! Try to make it until 11:30 :)


[setup]: # (assign participants to teams)

<!--
- Team 1 (file input, 3 persons): 
  - Team members: 
  - Task description: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise/task-file-input
- Team 2 (logging, 3 persons):
  - Team members: 
  - Task description: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise/task-logging
- Team 3 (average calculation, 3 persons):
  - Team members: 
  - Task description: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise/task-calculations
- Team 4 (median calculation, 3 persons):
  - Team members: 
  - Task description: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise/task-calculations
- Team 5 (median **low** calculation, 2 persons):
  - Team members: .
  - Task description: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise/task-calculations
- Team 6 (median **high** calculation, 3 persons): 
  - Team members:
  - Task description: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise/task-calculations
- Team 7 (square sum calculation, 3 persons):
  - Team members:
  - Task description: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise/task-calculations
- Team 8 (variance calculation, 3 persons):
  - Team members:
  - Task description: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise/task-calculations
- Team 9 (deviation calculation, 3 persons):
  - Team members:
  - Task description: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise/task-calculations
- Team 10 (product calculation, 3 persons):
  - Team members:
  - Task description: https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/tree/master/03_example-project/code/04_team-exercise/task-calculations
-->


### Step 2: Work on your Tasks
> If there are any problems write in the main room chat!
> You have normally time until you are finished! Try to make it until 11:30 :)

- Go to the break room:
    - Read the task details (5-10min)
    - Determine the "driver" 
    - Perform the tasks
- All teams perform these generic tasks
    - Create an issue
    - Create a merge request from the issue
  
[setup]: # (change link to gitlab-group)
  
  - Clone the Git repository of the team project: [https://gitlab.dlr.de/ws-sd-for-teams/YYYY-MM-DD/example-project-iteration-3](https://gitlab.dlr.de/ws-sd-for-teams/YYYY-MM-DD/example-project-iteration-3)
  - Switch to your feature branch
  - Perform the actual work
  - Commit and push changes
  - Review changes
  - Merge changes

### Step 3: Return to the Main Room when Ready :)
> If there are any problems write in the main room chat!
> You have normally time until you are finished! Try to make it until 11:30 :)


## Example Project | Iteration 3: Release Version 1.0.0 (Live Demonstration)
- [Iteration 3: Release Version 1.0.0](https://gitlab.com/hifis/hifis-workshops/software-development-for-teams/workshop-materials/-/blob/master/03_example-project/episodes/episode07.md)


## Reflecting your own Development Workflow
- Think about your development workflow (exercise day 1): What aspects would you change / apply after taking this workshop?


## Wrap up and Feedback Day 3



### Important Information
- Please fill out the post workshop survey which we send out with the workshop closing email :)
- HIFIS Software: [https://software.hifis.net](https://software.hifis.net)
- DLR Mattermost: [New ScienceDevs](https://mattermost.hzdr.de/signup_user_complete/?id=huu15rxw5jgsbdq8gifr771obh)
- DLR Wiki
