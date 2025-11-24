<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 4 - Set up the Build Pipeline

- Objective: Get started with GitLab CI
- Estimated time: 70min
- Teaching techniques: Live Coding

## Preparation

- Fork the project in your name space because we want to work on our own.
- Make sure that the issue tracker is activated: `Settings=>General=>Visibility, project features, permissions=>Issues`
- Remove the fork relationship: `Settings=>General=>Advanced=>Remove fork relationship`
- Create the new issue for the current task using the newly added `Change` issue template via `Issues=>New Issue`

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
Milestone: Release 0.2.0
Labels: type::enhancement
``` 

- Briefly name/explain pipeline basics (build runner, .gitlab-ci.yml) which we use next

## Set up the Build Runner

- Activate the build pipeline in `Settings=>General=>Visibility, project features, permissions=>Pipelines`
- Switch to `Settings=>CI / CD=>Runners` and explain a bit about the usual setup

## Set up the Basic Build Pipeline

- Switch to the created issue (`Issues`)
- Tick the first task
- Create a merge request from the issue
- Switch to the branch and create a new file:
    - Name: `.gitlab-ci.yml`
    - Show a template for `.gitlab-ci.yml` to give an impression about what we will do
- Explain the envisioned pipeline `test (all) => audit (all) => package (master)`:
    - `test`: Run tests on every supported platform to make sure our code works
    - `audit`: Run automated checks such as flake8, code coverage check etc.
    - `package`: Create a snapshot package and make artifacts available when the change is merged into the `master` branch
    - You can use CI lint to check your pipeline definition: ``<GITLAB PROJECT URL>/-/ci/lint``
    - Please see the [GitLab Help on GitLab CI](https://gitlab.com/help/ci/README.md) for further details
- Start from scratch and create the test stage:

```
# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


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

- Explain: job name, stage, script, image, tags, artifacts
- Commit: "Add initial test job"
- Show and explain `CI / CD => Pipelines` view
- Explain CI lint
- Switch to editing `.gitlab-ci.yml` and add the `audit` job and `stages`
    - Lint it before you add the custom stages
    - Bonus: Forget to add poetry install and show how the build fails


```
# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


stages:
  - test
  - audit

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

- Explain: stages, reason for additional poetry install (=> separate jobs / docker images)
- Commit: "Add audit job"
- Show and explain `CI / CD => Pipelines` view (=> connected stages)
- Switch to editing `.gitlab-ci.yml` and add the `snapshot` job:

```
# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


stages:
  - test
  - audit
  - package

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

snapshot:
  stage: package
  image: python:3.6
  script:
    - pip install poetry
    - poetry install
    - poetry version 0.2.0-alpha
    - make package
  tags:
    - docker
  only:
    - master
  artifacts:
    paths:
      - build
      - dist
      - docs/html
```

- Explain: only, artifacts
- Commit: "Add snapshot job"
- Show and explain `CI / CD => Pipelines` view (no snapshot because not merged yet)
- Switch to editing `.gitlab-ci.yml` and optimize the pipeline **if there is time**.
  Otherwise tell that it is possible to reuse pipeline code and to use caching.
  Participants can see it later in the team exercise.

```
# SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT


variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip
    - .venv
  key: "${CI_JOB_NAME}"

stages:
  - test
  - audit
  - package

before_script:
  - pip install poetry
  - poetry --version
  - poetry config virtualenvs.in-project true
  - poetry install -vv

test:
  image: python:3.6
  stage: test
  script:
    - make test
  tags:
    - docker
  artifacts:
    reports:
      junit: build/tests.xml

audit:
  image: python:3.6
  stage: audit
  script:
    - make audit
  coverage: '/^TOTAL.+?(\d+\%)$/'
  tags:
    - docker
  artifacts:
    expose_as: "Coverage Report"
    paths: ["build/htmlcov/"]

snapshot:
  stage: package
  image: python:3.6
  script:
    - poetry version 0.2.0-alpha
    - make package
  tags:
    - docker
  only:
    - master
  artifacts:
    paths:
      - build
      - dist
      - docs/html
```

- Explain: cache, variables, before_script
- Commit: "Optimize build pipeline"
- Show and explain `CI / CD => Pipelines` view (no snapshot because not merged yet)
- Merge the merge request (`Merge Requests`), remove `Closes`
- Show the pipeline view (`CI / CD`) => new pipeline for `master` branch
- Tick task 2 in the issue and reference merge request beside the task

### Add Badges to make Results easier accessible

- Switch to `Settings=>General=>Badges`
- Add Pipeline Status Badge:
    - Link: `<PROJECT URL>/commits/master`
    - Image URL: `<PROJECT URL>/badges/master/pipeline.svg`
- Add Code Coverage Badge:
    - Link: `<PROJECT URL>/commits/master`
    - Image URL: `<PROJECT URL>/badges/master/coverage.svg`
- Add Artifact Download:
    - Link: `<PROJECT URL>/-/jobs/artifacts/master/download?job=snapshot`
    - Image URL: `https://img.shields.io/badge/Artifacts-Download-brightgreen.svg`
- Tell the following:
    - Pipeline Status / Code Coverage links can be found in: `Settings=>CI / CD=>General Pipelines`
    - Artifact download URLs for job artifacts, please see: https://gitlab.com/help/ci/pipelines/job_artifacts.md#downloading-the-latest-artifacts
    - Show https://img.shields.io as a service to generate badge images
- Tick task 3 in the issue
- Close the issue

## Key Points

- GitLab CI offers a straight-forward way to get started with integration builds and build pipelines.
- Make sure that you have a good build script as basis and do not try to "program yaml".
- To make results visible, you can already use features such as code coverage display and badges.
  And there is much more to discover!
