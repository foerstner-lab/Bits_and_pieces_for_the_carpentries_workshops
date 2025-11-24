# SPDX-FileCopyrightText: 2021 German Aerospace Center (DLR)
# SPDX-License-Identifier: MIT
#
# Purpose: Defines issues, milestones, labels, and badges for the third iteration.
# Requires: Python >= 3.9, python-gitlab >= 4.2
# Usage:
#   - Install the dependencies
#   - Define a configuration file `gitlab-config.ini` with a section `gitlab4teams` as explained here: https://python-gitlab.readthedocs.io/en/latest/cli-usage.html#configuration, require GitLab access token with scope API
#   - Define the project ID of the GitLab project `Example Project - Iteration 3` in variable `_PROJECT_ID`
#   - Run the script


import gitlab


_PROJECT_ID = 0 # Please set the PROJECT ID


# Authenticate with the GitLab instance
glab_api = gitlab.Gitlab.from_config("gitlab4teams", config_files=["gitlab-config.ini"])
glab_api.auth()
project = glab_api.projects.get(_PROJECT_ID)

# Define labels
labels = project.labels.list() or [
    project.labels.create(label)
    for label in [
        { "name": "type::feature", "color": "blue", "description": "Marks new features" },
        { "name": "type::bug", "color": "orange", "description": "Marks errors" },
        { "name": "type::enhancement", "color": "blue", "description": "Marks improvements" },
        { "name": "type::release", "color": "blue", "description": "Marks release preparations" },
        { "name": "component::calculation", "color": "green", "description": "Marks tasks related to calculations" },
        { "name": "component::inputs", "color": "green", "description": "Marks tasks related to input methods" },
    ]
]

# Define milestones
milestones = project.milestones.list()[::-1] or [
    project.milestones.create(milestone)
    for milestone in [
        { "title": "Release 0.1.0", "description": "Capture results of iteration 1" },
        { "title": "Release 0.2.0", "description": "Capture results of iteration 2" },
        { "title": "Release 1.0.0", "description": "Capture results of the initial release" },
    ]
]

# Define issues
issues = project.issues.list(state='opened') or [
    project.issues.create(issue)
    for issue in [
        {
            "title": "Implement end-to-end prototype",
            "description": "...",
            "milestone_id": milestones[0].id,
            "labels": ["type::feature"],
        }, {
            "title": "Implement object oriented design",
            "description": "...",
            "milestone_id": milestones[1].id,
            "labels": ["type::feature"],
        }, {
            "title": "Implement calculations",
            "description": "...",
            "milestone_id": milestones[2].id,
            "labels": ["type::feature", "component::calculation"],
        }, {
            "title": "Implement sum calculation",
            "description": "...",
            "milestone_id": milestones[1].id,
            "labels": ["type::feature", "component::calculation"],
        }, {
            "title": "Implement input sources",
            "description": "...",
            "milestone_id": milestones[2].id,
            "labels": ["type::feature", "component::inputs"],
        }, {
            "title": "Implement command line interface",
            "description": "...",
            "milestone_id": milestones[1].id,
            "labels": ["type::feature", "component::inputs"],
        },
    ]
]

# Fine tune issues
for ms, ms_issues in [
    (milestone, [issue for issue in issues if issue.milestone and issue.milestone["id"] == milestone.id])
    for milestone in milestones[:2]
]:
    for issue in ms_issues:
        issue.state_event = 'close'
        issue.save()

    ms.state_event = 'close'
    ms.save()

# Define project badges
badges = project.badges.list() or [
    project.badges.create(badge)
    for badge in [
        {
            "link_url": glab_api.url + "/%{project_path}/commits/%{default_branch}",
            "image_url": glab_api.url + "/%{project_path}/badges/%{default_branch}/pipeline.svg",
        }, {
            "link_url": glab_api.url + "/%{project_path}/commits/%{default_branch}",
            "image_url": glab_api.url + "/%{project_path}/badges/%{default_branch}/coverage.svg",
        },
    ]
]
