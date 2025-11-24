<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 1 - Explain the Project Context and our Tasks

- Objective: Explain the project context
- Estimated time: 30min
- Teaching techniques: Presentation, Live Demonstration

## Explain the Project Context

### Sample Calculator

- Sample Calculator is a command line tool / library to calculate characteristic values of a sample.
- Functional requirements:
  - Implement reading sample values from console and files (CSV format)
  - Implement calculation of average, variance, standard deviation as well as other calculations
  - Implement logging of all relevant steps (console output, log files)
- Quality requirements:
  - Easily extensible with regard to calculations
  - Easily extensible with regard to input methods
- Constraints:
  - Python >=3.6, no additional dependencies for usage
  - Iterative development approach

### Iterative Development Approach

- Time-boxed iterations
- Iteration process: Planning => Implementation => Closing
- Initially, there are 3 iterations planned:
  - Iteration 1: End-to-end prototype to find out the pitfalls
  - Iteration 2: Initial design, build script, change process
  - Iteration 3: Release 1.0.0 which fulfills quality requirements and provides some of the calculations
- Current status:
  - Iteration 1 has been successfully performed
  - We are in the middle of iteration 2

## Explain the current Status and our Tasks

- Initial design including basic implementation, tests, build script
  documentation is already there
    - Show the GitLab project for iteration 2
    - Focus on: repository structure, developer guide, build script, principles
- We are responsible for:
    - Setup of the issue tracker
    - Setup of the build pipeline
- Explain the current change process and explain the missing bits that we are responsible for.

## Key Points

- We are in the middle of the Sample Calculator development.
- We are responsible to set up the supporting infrastructure for the project.
