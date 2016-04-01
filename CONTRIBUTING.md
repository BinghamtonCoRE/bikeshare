#Contributing to BUBS

Thanks for being interested in contributing, and checking to find out the best way to do it!

Use the following set of guidelines to help streamline the process of contributing to BUBS. These aren't rules or laws, so they may not always be the best option. Feel free to propose changes to them as well.

####Table of Contents
[How to Contribute](#how-to-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Feature Requests](#feature-requests)
  * [Contributing Code](#contributing-code)
  * [Pull Requests](#pull-requests)

[Appendix](#appendix)
  * [Style Guide](#style-guide)
  * [Tags Guide](#tags-guide)

##How to Contribute

###Reporting Bugs
Please try to adhere to the following guidelines when submitting a bug report for BUBS. Keeping reports clean and succinct helps us identify and solve problems quickly and effectively!

####Before Submitting a Bug Report
  * **Check to find out what branch you're on.** If you're working in the develop branch, make sure you're pulled and up to date. If you're on master (or on the main site) then it's probably a bug.
  * **Don't submit duplicates.** Check through the [current open issues](https://github.com/BinghamtonCoRE/bikeshare/issues) tagged with `bug` to see if the problem you've found has already been reported.
    * **Add more information if there is something missing.** If you find an already open bug report, feel free to comment with more information.

####Submitting a Good Bug Report
We track our bugs as [Github issues](https://guides.github.com/features/issues/). Once you've figured out which repository the bug is from, open up an issues in the repository and add as much of the following information that you can.
* **A descriptive title** to help us figure out who should be tackling the problem.
* **Describe how to reproduce the problem** in as much painstaking detail as possible. Is the issue only happening to you or is it happening for others? How often does it happen? If you can reproduce the issue, **list the steps to do so in as much detail as possible**.
* **Describe the behavior of the bug.** What did you expect to happen vs what actually did happen.
* **Screenshots or gifs are great.** A picture is worth a thousand words, so a moving one is probably worth a lot.
* **If you cant reproduce the problem** try to explain exactly what you were doing before it happened.

Include relevant details about the environment in which you're using BUBS
* **What browser are you using?**
* **Are you using the virtual environment?** Also include the version of Python you're on.
* **Your operating system.**

###Feature Requests
Follow the guidelines when submitting feature requests to help move everything along.

####Before Submitting an Enhancement
* **Make sure you're up to date.** Maybe the enhancement has already been added!
* **Check open issues.** Look for issues tagged with `enhancement` to see if someone has already suggested it.

####Submitting a Good Feature Request
* **Include a clear and descriptive title.**
* **Provide a step-by-step description** to demonstrate what the enhancement is and how it works.
* **Provide specific examples** to demonstrate how your steps work.
* **Describe the current behavior** if there is any. Also explain what the new behavior should be and why.
* **Include screenshots and gifs.**
* **Link to or describe other applications** where a similar feature exists (if there is one).

###Contributing Code
If you're unsure about how to contribute to begin contributing to BUBS, have a look at some open issues tagged with `help-wanted` or `beginner`.

* [Beginner](https://github.com/BinghamtonCoRE/bikeshare/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3Abeginner) - These issues *should* be relatively easy and are a good place to start trying to contribute.
* [Help Wanted](https://github.com/BinghamtonCoRE/bikeshare/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22+) - These issues may be more involved and are currently unclaimed, or looking for others to help.

###Pull Requests
* If you include changes to frontend you should probably include screenshots.
* Run pylint on your code while developing as this is what we use during our Travis Build
* Follow [PEP8 standards](https://www.python.org/dev/peps/pep-0008/) when adding new code
* Code should not fail unit tests unless for a good reason
* Include helpful docstring comments. See the [Style Guide](#style-guide) in the appendix.
* Tag it appropriately. See the [Tags Guide](#tags-guide) in the appendix.
* `# TODO ...`'s are ok, but there should probably be an issue opened for them if they are merged.

##Appendix

###Style Guide
This section has information on how the code should be styled.

####General
* 79 characters or less per line
* Docstrings and comments should be 72 characters or less
* Use four spaces rather than tab characters
* Surround function and class definitions with two blank lines
* imports should be on separate lines, unless importing multiple items from one module
* Imports should be in the following order:
  * Standard library
  * Third party libraries
  * Local libraries
* Use single quotes (`'`) for strings
* Use the new format method for strings. `'foo = {}'.format(16)`

####Pet Peeves
* No whitespace inside parethesis or brackets. `foo(arg1, arg2)` instead of `foo( arg1, arg2 )`.
* No whitespace before a comma, semicolon or colon.
  * *Unless* it's acting like a binary operator like the `:` for a slice. In this case the whitespace must be the same on both sides. Less whitespace is preferred, however whitespace may be added for readability.
* No whitespace before the argument list of a function call. `foo(arg1)` rather than `foo (arg1)`.
* No extraneous whitespace around an assignment (or other) operator to align them.
```
x = 1          | x        = 1
y = 2          | y        = 2
long_var = 3   | long_var = 3
```

####Functions
Function names should be `snake_case` and leave the closing parenthesis on the same line.
```
foo = long_function_name(var_one, var_two
                         var_three, var_four)
```
If the function name is very long and the parameters can't fit on the same line use the following style:
```
def really_long_function_name_no_params_fit(
        var_one, var_two
        var_three, var_four):
    print('Hello world!')
```

* Don't put spaces around the `=` for default parameters `def foo(bar='no space')`
  * Don't make lists or dictionaries default values

####Lists and Dictionaries
List and dictionaries should have the brace/parenthesis on the next line and always have a trailing comma on the last element.
```
foo = [
    a, b, c,
    d, e, f,
]
```

###Tags Guide
####Issue Type and State
| Label Name | Description |
| --- | --- |
| `enhancement` | Feature request. |
| `bug` | Confirmed bug or something that is likely a bug. |
| `question` | Community question. |
| `help-wanted` | This issue is likely unclaimed and we could use some help working on it. |
| `beginner` | Less complex issues which would be good first issues for people to get involved with. |
| `blocked` | Blocked waiting for another issue. |
| `duplicate` | Duplicate of another issue. |
| `wontfix` | Issue wont be fixed because it's working as intended or for some other reason. |
| `invalid` | Issue is invalid. (user error) |

####Categories
| Label Name | Description |
| --- | --- |
| `documentation` | Related to the documentation. |
| `security` | Related to security. |
| `ui` | Related to frontend or user interfaces. |
| `crash` | Caused the app to totally crash. |
| `git` | Related to git functionality. (gitignore problems usually) |

####Pull Request Labels
| Label Name | Description |
| --- | --- |
| `work-in-progress` | Pull request is still being worked on, expect changes to follow. |
| `needs-review` | Pull request still needs a review from one of the contributors. |
| `under-review` | A contributor is reviewing this pull request. |
| `requires-changes` | A contributor has requested changes to be made to this pull request. |
