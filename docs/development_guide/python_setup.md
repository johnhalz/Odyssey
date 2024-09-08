# Python Environment Setup

As Odyssey is a Django project (written in python). It is recommended to use a virtual environment to handle the project's dependencies.

## Installing Python
To install python on your machine, it is recommended to use [pyenv](https://github.com/pyenv/pyenv) (or [pyenv-win](https://github.com/pyenv-win/pyenv-win) for Windows).

After having installed pyenv, you can install a specific version on your machine by running:

``` sh
pyenv install 3.11.7
```

We recommend to install python 3.11.7 or later, as Odyssey was built using python 3.11.7.

## Creating a Virtual Environment with Poetry

### Installing Poetry

For creating a virtual environment, we recommend to use [poetry](https://python-poetry.org/), as Odyssey was built using this tool as well.

After having installed Poetry on your system, it is highly recommended to enable the [`virtualenvs.in-project` configuration option](https://python-poetry.org/docs/configuration/#virtualenvsin-project). You can do this by running the following command:

``` sh
poetry config virtualenvs.in-project true
```

This will make Poetry create `.venv` files in the project folder, making it much easier to manage the virtual environments that Poetry creates.

### Installing Dependencies and Creating Virtual Environment

After having cloned this repo, you can install all dependencies and create a virtual environment by just running the command:

``` sh
cd <path-to-odyssey-folder>
poetry install --group dev
```

This will install all required dependencies (listed in the `pyproject.toml` file).

All that’s left now is to add the [seed data to the database](./Making%20Migrations%20&%20Adding%20Seed%20Data.md)!

----

# Reference Links:
- [pyenv Documentation (README)](https://github.com/pyenv/pyenv#table-of-contents)
- [poetry Documentation](https://python-poetry.org/docs/)