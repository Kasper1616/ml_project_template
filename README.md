# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Overview

This project is a machine learning template designed to streamline the development of ML workflows. It uses [Cookiecutter](https://cookiecutter.readthedocs.io/) to generate a structured project layout, ensuring consistency and best practices.

## Features

- **Modular Codebase**: Organized into reusable components for data processing, model training, evaluation, and visualization.
- **HPC Job Scripts**: Predefined scripts for running training and evaluation on GPU clusters.
- **Testing**: Includes unit tests for data and model components.
- **Development Tools**: Pre-configured with `invoke` tasks, `pre-commit` hooks, and linting tools like `ruff`.
- **Documentation**: Ready to use with `mkdocs` for generating project documentation.

## Project Structure

```txt
├── data/                     # Data directory
│   ├── processed/            # Processed data
│   └── raw/                  # Raw data
├── jobs/                     # HPC job scripts
│   ├── evaluate.sh           # Script for evaluation on GPU
│   └── train.sh              # Script for training on GPU
├── models/                   # Trained models
├── notebooks/                # Jupyter notebooks
├── reports/                  # Reports
│   └── figures/              # Generated figures
├── {{ cookiecutter.project_name }}/  # Main project code
│   ├── __init__.py           # Package initialization
│   ├── data.py               # Data processing utilities
│   ├── evaluate.py           # Model evaluation
│   ├── model.py              # Model definition
│   ├── train.py              # Model training
│   └── visualize.py          # Visualization utilities
├── tests/                    # Unit tests
│   ├── __init__.py
│   ├── test_data.py          # Tests for data processing
│   └── test_model.py         # Tests for model
├── .gitignore                # Git ignore file
├── pyproject.toml            # Python project configuration
├── README.md                 # Project README
├── requirements.txt          # Project dependencies
├── requirements_dev.txt      # Development dependencies
└── tasks.py                  # Invoke tasks for automation
```

## Getting Started

### Installation

1. Generate a new project using Cookiecutter:

   ```sh
   cookiecutter https://github.com/kasper1616/ml_project_template.git
   ```

2. Navigate to the generated project directory:

   ```sh
   cd {{ cookiecutter.repo_name }}
   ```

3. Create a Conda environment:

   ```sh
   invoke create-environment
   ```

4. Install dependencies:

   ```sh
   invoke requirements
   ```

5. Install development dependencies (optional):

   ```sh
   invoke dev-requirements
   ```

### Usage

#### Preprocess Data

Run the data preprocessing script:

```sh
invoke preprocess-data
```

#### Train the Model

Train the model locally:

```sh
invoke train
```

Train the model on an HPC cluster using GPUs:

```sh
invoke train-gpu
```

#### Run Tests

Run all unit tests:

```sh
invoke test
```

#### Lint and Format Code

Run `ruff` to lint the code:

```sh
ruff {{ cookiecutter.project_name }}
```