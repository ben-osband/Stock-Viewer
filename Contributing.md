# Overview

To make additions to the project, first make sure you are added as a collaborator and then follow these steps:

* Add a branch
* Make changes and commit to the branch
* Merge the branch with the main branch

## Adding a Branch

You can add branches either [through GitHub](#-adding-through-github) or [through the Git Bash](#-adding-through-git-bash)

_Note: Branches should be written in all lowercase, have dashes instead of spaces, and be descriptive of what is being done. e.x. 'plot-replacement-issue'_

### Adding Through GitHub

To add a branch through the GitHub website, start by going to the main page of the repository and click where it says the number of branches.

![Branches Button](Public/Images/branches-button.png)

Then click the green **New branch** button, give your new branch a name and a source, and then click **Create branch**

Now that you have created the new branch, open the Git Bash and type 

```
git pull
```

to get the new branch from the remote and then `git status` to check what branch you are in

If you are not in the correct branch, type 

```
git checkout branch-name
```

### Adding Through Git Bash

To add a branch through Git Bash, start by opening the Git Bash in your local repository

In the terminal, first type `git status` to make sure you are in the main branch

Then, to create a new branch, type 

```
git checkout -b branch-name
```

## Making Commits

Making commits to a branch is exactly the same as making commits to the main branch. Before you make any commits, though, type `git status` to make sure you are in the correct branch.

As a review, here is how to make a commit:

```
git add .
git commit -m "description"
```

## Pushing a Branch to the Remote

If you want to make the commits you have made to a branch show up on the remote, you have to make a push.

Pushing a branch to the remote is the same as pushing the main branch to the remote, but instead of typing

```
git push origin main
```

you would type

```
git push origin branch-name
```

## Merging Branches

You don't want to merge branches until you are done making changes

When you are ready to merge, make sure the working tree for the branch you've been working in is clean by typing

```
git status
```

if the working tree is not clean, type

```
git add .
git commit -m "description"
```

once the working tree is clean and all changes have been commited, change to the branch you want to merge into (main) by typing

```
git checkout main
```

and finally merge the branches by typing

```
git merge branch-name
```

_Note: When you merge, there may be conflicts that need to be handled_

## Deleting branches

You can delete remote branches from GitHub

To delete a local branch, you can type either

```
git branch -d branch-name
```

OR

```
git branch -D branch-name
```
