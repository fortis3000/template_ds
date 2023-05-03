Standartized DS project template
==============================

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py



--------



====

## Concept
## Goals
- Reduce time to establish a repo specifically for DS needs.
- To align data scientists in terms of skills and tools used.
- Make project standard, easier to observe and predictable.

## Description:

### Project structure

The current architecture is based on [Cookicutter DS](https://github.com/drivendata/cookiecutter-data-science) appoach. The reasoning behind it you can find [here](http://drivendata.github.io/cookiecutter-data-science/).

### Code versioning tools
To track, keep and share your codings [git](https://git-scm.com/) and [GitHub](https://github.com/) services are required.

### Default programming language
To leverage modern programming stack it is recommended to start with [Python 3.10](https://www.python.org/downloads/release/python-3100/) as default.

### Dependency management
To follow Single-Source-Of-Truth concept it makes sense to use `pyproject.toml` to store project configuration. `pyproject.toml` configuration file allows to use the same configuration on different project steps: CI/CD, dev, test, prod etc.

To manage Python dependencies using the same file we can use [poetry](https://python-poetry.org/).


### Codestyle: isort, black, pylint

The main idea is to make code style checking:

- Sufficient. Different parts of the code style suite are responsible for different code characteristics and neither of them can substituite all of them.
- Modular. In future it is possible to change some parts of the code style suite without affecting other parts, e.g. pylint -> ruff, isort -> reorder-python-imports etc.
- Separate from dev, test, prod and other environments. The linting and formatting tool are used only on checking stage and are redundant for other Docker images.

To apply code style suite easily, use `make precommit` command. You can find a set of commands in `Makefile`.

The current code style suite includes following stages:

#### isort
Use [isort](https://pycqa.github.io/isort/) to keep your imports in order. The library takes its configuration from `pyproject.toml`, section `[tool.isort]`

#### black
Use [black](https://github.com/psf/black) formatter for stable code formatting rules. The library takes its configuration from `pyproject.toml`, section `[tool.black]`

#### pylint
Use [pylint](https://pypi.org/project/pylint/) to analyse your Python code.

Note that pylint keeps its configurations in separate file `.pylinrc`. For more convinience the general template of this file was added to the project template.

### CI/CD: GitHub Actions

As a baseline, CI with integrated code style is provided (see `.github/workflows/ci.yml`). The current setup is based on using public Actions and configurating CI with `pyproject.toml` file. It is also possible to use corporate Actions.

### Test suite:
TO BE DONE (pytest)


## Getting started
1. Create repo from the template

While creating repo, choose the current one as a template. Check [tutorial](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) for more details.

2. Install poetry

The recommended way to install poetry and aviod additional issues is to install it with pip. Check the [link](https://python-poetry.org/docs/#installing-manually) for exact commands. In CI it is possible to use [poetry Action](https://github.com/marketplace/actions/python-poetry-action)

3. Change parameters `pyproject.toml` if needed.
4. Put you source code in `src` folder.
5. Tweak CI configuration `.github/workflows/ci.yml` if needed.
6. Enjoy coding :)

## Best practices
TO BE DONE
### Makefile
### Cli with typer
