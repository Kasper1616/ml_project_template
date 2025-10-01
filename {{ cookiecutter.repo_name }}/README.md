# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Project structure

The directory structure of the project looks like this:
```txt                 
├── data/                     # Data directory
│   ├── processed
│   └── raw
├── jobs/                     # HPC job scripts
│   ├── evaluate.sh
│   └── train.sh
├── models/                   # Trained models
├── notebooks/                # Jupyter notebooks
├── reports/                  # Reports
│   └── figures/                     
├── project_name/             # Main project
|   ├── __init__.py
│   ├── data.py
│   ├── evaluate.py
│   ├── models.py
│   ├── train.py
│   └── visualize.py
└── tests/                    # Tests
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_data.py
│   └── test_model.py
├── .gitignore
├── pyproject.toml            # Python project file
├── README.md                 # Project README
├── requirements.txt          # Project requirements
├── requirements_dev.txt      # Development requirements
└── tasks.py                  # Project tasks
```
