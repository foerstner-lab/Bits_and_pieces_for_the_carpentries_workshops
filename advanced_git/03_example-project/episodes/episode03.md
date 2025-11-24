<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 3 - Introduction to Build Automation

- Objective: Introduce the concepts build process, build script and build pipeline
- Estimated time: 20min
- Teaching techniques: Presentation

## Explain the basic Idea of the Build Process and the Build Script

- The `build process` transforms the source elements into a usable package and performs different checks on them.
- The `build script` implements the build process.
  Typically, a specific scripting technology (e.g., bash, MakeFiles, CMake, ...) is used to implement the build script.
- The build process of the example project is implemented by a Makefile and
  provides build targets to run tests, check various things, as well as to create an installable package.
- Developers can use the build script to quickly check their local changes (local build).
  In addition, it is used to perform user-unattended integration builds.
  These builds are typically run by a server using a neutral reference build environment and
  make sure that the changes of different developers are working when combining them.
- The build script helps to ensure software quality as well as to improve productivity.

## Explain the Basics of a Build Pipeline

- A `build pipeline` is a way to establish an integration build for your software project.
  It can even be extended to automate the deployment as well.
- Draw an example (e.g., `build => test => deploy`) and explain the basic concepts
  - A build pipeline consists of different stages which are executed from left to right.
  - For every new change, the build pipeline will be started.
  - Only if one stage is completed successfully, the next stage will start.
  - If a change completes all stages successfully, it can be considered as "ready to use".
  - We want to make sure that errors are found as early as possible (i.e. in early stages) to provide quick feedback to the developers.
- GitLab provides a way to implement such a build pipeline:
  - Stages are executed from left to right (default behavior).
  - Every stage can have multiple build jobs.
  - A `build job` is an atomic unit of work (e.g., run tests, check code formatting).
  - All build jobs must succeed before the next stage starts (default behavior).
  - All build jobs of a stage can run in parallel (default behavior).

## Key Points

- The build process transforms the source elements into a usable package and performs different checks on them.
- The build script automates the build process and helps to ensure software quality as well as to improve productivity.
- Build pipelines makes sure that those checks are performed at the right time and
  can be even extended to automate the deployment as well.
