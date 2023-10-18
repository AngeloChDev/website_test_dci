# Coding Standards

## Topics covered

Code styling and static analysis tools.

## Goal achieved 

By the end of the exercise you will have adapted your code to a standard style that may make it more readable and usable by other developers.

## Description

If you haven't done it already, create a virtual environment and install flake8 to run it against the entire basecode (including both the `cli` and `tests` directories).

Once you get the output, address each issue until the output of flake8 returns no error.

> In some exceptional cases you may want to use the `#no-qa` tag to skip a particular issue. This should only be done when you have no other alternative.

Once flake8 returns no issue, install isort and run it.

Then install the flake8 plugins `pep8-naming` and `flake8-docstrings`. Run `flake8` again and fix the issues.

Finally, install and run `black`.
