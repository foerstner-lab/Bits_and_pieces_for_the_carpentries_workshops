#!/bin/bash
# SPDX-FileCopyrightText: 2021 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT
#
# Purpose: Initializes the Sample Calculator Git repository for the initial iteration.
# Requires: Bash shell environment, git client
# Usage hint: Configure Git URLs before usage.


TARGET_GIT_URL= # PLEASE ADAPT
SOURCE_GIT_URL="https://codebase.helmholtz.cloud/hifis/software/education/hifis-workshops/software-development-for-teams/sample-calculator.git"


mkdir example-project-iteration-1
cd example-project-iteration-1
git init -b main
git remote add template $SOURCE_GIT_URL
git fetch template
git merge remotes/template/01a-initial-prototype
git remote remove template
git tag --delete 1.0.0 0.2.0 0.1.0
git prune
git remote add origin $TARGET_GIT_URL
git push --tags origin main
cd ..
