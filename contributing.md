# Contributing

This project implements a [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause),
 specified within [`license.md`](https://github.com/jeff1evesque/machine-learning/blob/master/license.md).

## Creating an Issue

### Issue: Title

Depending on circumstance: a descriptive, or non-descriptive issue title is
 acceptable.

The following is an example of a descriptive issue title:

```text
index.php, include 'header.php'
```

More specifically, the following rules of a descriptive issue title *must* be
 followed:

- an issue title should *never* be over 50 characters
- an issue title should *never* contain possessive tones
- filename reference(s) in the issue title, should *always* be wrapped by
 single quotes

Otherwise, a non-descriptive issue title can be used as follows:

```text
Implement flask upstart script
```

A non-descriptive issue title is generally used, when multiple files will be
 modified in a single pull request.  Therefore, remember to capture the
 technology, or item(s) that will be implemented in less than 50 characters
 (without possessive tone).

### Issue: Body

- filename references should *always* be wrapped by single tildas
- codeblocks should *always* be wrapped by triple tildas
 ([fenced code block](https://help.github.com/articles/creating-and-highlighting-code-blocks/#fenced-code-blocks)), where the first set of triple tildas is followed by the
 language being used ([syntax highlighted](https://help.github.com/articles/creating-and-highlighting-code-blocks/#syntax-highlighting))
- one line code snippets must be wrapped by single tildas
 ([inline format](https://help.github.com/articles/basic-writing-and-formatting-syntax/#quoting-code))
- when referring to another issue, always provide a reference to it. This can
 be done by either [linking](https://help.github.com/articles/autolinked-references-and-urls/#issues-and-pull-requests)
 keywords within *issue body*, or by simply providing the issue number (i.e. `#230`)

## Creating GIT Branch

Branch names must be categorized into the following categories:

- bug: an existing feature contains a problem
- feature: any new, or enhanced feature
- remove: one or more file(s), or directory need to be removed

More specifically, branches should be named as follows:

- `bug-[issue number]`
- `feature-[issue number]`
- `remove-[issue number]`

Therefore, an issue should be created prior to creating a new branch.  Once the
 branch has been created, the corresponding branch can be created as follows:

```bash
git checkout -b [bug|feature|remove]-[issue number] master
```

**Note:** the `[issue number]` should be an integer, without special characters.

## Committing Code

When creating a *commit*, be sure to include an issue number, the filename (preferred)
 modified, and a short message.

The following git commit message, is an acceptable syntax:

`git commit -m "#230: index.php, implemented 'strtotime()' function"`

The message should *always* be prefixed with an issue number that the commit
 corresponds to. When all components are factored in, the commit message should
 *never* be more than 50 characters long, *never* be in a possessive tone, and
 any references to a file, or method *should* be wrapped by a single quote.

**Note:** commits should be granular, such that, every commit corresponds to a
 small change within *one* file. In some cases, when a commit spans multiple
 files, when changes are very similar, or when merging one branch, into the
 current branch, the filename can be omitted:

```text
#2844: conform boolean values to python syntax
```

## Creating Pull Request

### Pull Request: Title

The following pull request title, is an acceptable syntax:

```text
#230: index.php, included 'header.php'
```

More specifically, the following rules *must* be followed:

- a pull request title should *always* begin with the issue number, and the
 file modified
- a pull request title should *never* be over 50 characters (including the
 *issue number*)
- a pull request title should *never* contain possessive tones
- filename reference(s) in the pull request title, should *always* be wrapped
 by single quotes

**Note:** in some cases, the filename is longer than usual, or the corresponding
 issue spans multiple files. In these cases, the filename can be omitted from
 the pull request title:

```text
Add ability to create randomized sub-datasets
```

### Pull Request: Body

Always include one of the following [*keywords*](https://help.github.com/articles/closing-issues-via-commit-messages/#keywords-for-closing-issues)
 followed by the *issue number* in a pull request body:

- Close
- Closes
- Closed
- Fix
- Fixes
- Fixed
- Resolve
- Resolves
- Resolved

For example, including `Resolves #230` in the *pull request* body, will
 automatically close issue `#230` when the *pull request* is merged.
