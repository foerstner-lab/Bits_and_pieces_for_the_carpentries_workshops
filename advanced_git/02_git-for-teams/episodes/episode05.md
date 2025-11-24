<!--
SPDX-FileCopyrightText: 2020 German Aerospace Center (DLR)

SPDX-License-Identifier: CC-BY-4.0
-->

# Episode 5 - Conflicts

- Objective: Learn about dealing with merge conflicts
- Estimated time: 45min
- Teaching techniques: Live Coding

## Create a Conflict

Here we show how conflicts can be handled with the Git command line client.

### Create a Feature Branch (step 1)

- Create the new branch `add-license-placeholder` and switch to it via: `git checkout -b add-license-placeholder` (Git version >= 2.23 supports: `git switch -c <BRANCH NAME>`)
- Add [LICENSE.md](../code/05_conflicts_step-1/LICENSE.md) from workshop materials
  - `git add LICENSE.md`
  - `git commit -m "Add license template"`
  - Verify with `git graph`

```
      o <- HEAD, add-license-placeholder
     /
o - o <- master
```

### Stash the current Work

- Add reference to `LICENSE.md` in the `README.md` at the bottom of the file:
```
## License

Please see the file [LICENSE.md](LICENSE.md) for further information about how the content is licensed.
```
- Tell that we were informed to quickly change something on the `master` branch
- Show that `git stash` has an empty stack of work via: `git stash list`
- Show difference on current feature branch
  - `git diff`
  - Our changes are returned as expected
- Temporally save the work to the stack via: `git stash`
- Show that we created a new entry on stack via: `git stash list`
- Show difference on current feature branch
  - `git diff`
  - No changes are returned, since the work was stashed

### Fix something on `master` (step 2)

- Switch to branch `master` via: `git checkout master` (Git version >= 2.23 supports: `git switch <BRANCH NAME>`)
- Add reference to contributors into README.md
  - Add [README.md](../code/05_conflicts_step-2/README.md) from workshop materials 
  - `git add README.md`
  - `git commit -m "Reference contribution guidelines and changelog"`
  - Verify with `git graph`

```
      o <- add-license-placeholder
     /
o - o - o <- HEAD, master
```

### Apply stashed Work on the Feature Branch

- Switch to branch `add-license-placeholder` to complete our work via: `git checkout add-license-placeholder` (Git version >= 2.23 supports: `git switch <BRANCH NAME>`)
- Review the stashed changes via: `git stash show STASHID`
- Retrieve and apply the stashed changes via: `git stash pop`
- Show local changes on feature branch
  - `git diff`
  - Our changes are now applied from the stack to the current branch
- Add and commit change in `README.md`
  - `git add README.md`
  - `git commit -m "Add license placeholder"`
  - Verify with `git graph`


```
      o - o  <- HEAD, add-license-placeholder
     /
o - o - o <- master
```

### Abort a Merge

- Switch to branch `master` via: `git checkout master` (Git version >= 2.23 supports: `git switch <BRANCH NAME>`)
- Merge `add-license-placeholder` into branch `master` via: `git merge add-license-placeholder`
- Show repository status
  - `git status`
  - Highlight that only `README.md` has a conflict
  - Explain that Git is aware of the merge and highlight merge status in the command line interface
  - Highlight that these conflicts can occur when rebasing, if the same files were changed
- Show how to **Abort** a merge via: `git merge --abort`
- Show that repository is clean again via: `git status`


### Merge by resolving the Conflicts

- Merge branch `add-license-placeholder` into the `master` branch
  - `git merge add-license-placeholder`
  - Resolve conflicts manually
  - `git add README.md`
  - `git commit`

```
      o - o <- add-license-placeholder
     /     \
o - o - o - o <- HEAD, master
```

### Clean up

- Delete branch `add-license-placeholder`, since it is merged, via: `git branch -d add-license-placeholder`

## Key Points

- Conflicts occur when two or more persons change the same file(s) at the same time.
- Conflicts can occur when a branch is rebased onto another branch.
- Git does not allow people to overwrite changes blindly, but highlights conflicts so that they can be resolved.
