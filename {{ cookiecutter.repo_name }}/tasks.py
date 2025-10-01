import os

import cookiecutter

from invoke import Context, task

WINDOWS = os.name == "nt"
PROJECT_NAME = {{ cookiecutter.project_name }}
PYTHON_VERSION = {{ cookiecutter.python_version }}

# Setup commands
@task
def create_environment(ctx: Context) -> None:
    """Create a new conda environment for project."""
    ctx.run(
        f"conda create --name {PROJECT_NAME} python={PYTHON_VERSION} pip --no-default-packages --yes",
        echo=True,
        pty=not WINDOWS,
    )

@task
def requirements(ctx: Context) -> None:
    """Install project requirements."""
    ctx.run("pip install -U pip setuptools wheel", echo=True, pty=not WINDOWS)
    ctx.run("pip install -r requirements.txt", echo=True, pty=not WINDOWS)
    ctx.run("pip install -e .", echo=True, pty=not WINDOWS)


@task(requirements)
def dev_requirements(ctx: Context) -> None:
    """Install development requirements."""
    ctx.run('pip install -e .["dev"]', echo=True, pty=not WINDOWS)

# Project commands
@task
def preprocess_data(ctx: Context) -> None:
    """Preprocess data."""
    ctx.run(f"python src/{PROJECT_NAME}/data.py data/raw data/processed", echo=True, pty=not WINDOWS)

@task
def train(ctx: Context) -> None:
    """Train model."""
    ctx.run(f"python src/{PROJECT_NAME}/train.py", echo=True, pty=not WINDOWS)

@task
def test(ctx: Context) -> None:
    """Run tests."""
    ctx.run("coverage run -m pytest tests/", echo=True, pty=not WINDOWS)
    ctx.run("coverage report -m -i", echo=True, pty=not WINDOWS)

@task
def train_gpu(ctx: Context) -> None:
    """Train model using GPU."""
    ctx.run(f"bsub < jobs/train_gpu.sh", echo=True, pty=not WINDOWS)

@task
def test_gpu(ctx: Context) -> None:
    """Test model using GPU."""
    ctx.run(f"bsub < jobs/test_gpu.sh", echo=True, pty=not WINDOWS)