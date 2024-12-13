# mlops-end-to-end

# Prerequisites 
## Create Anaconda (or miniconda) environment
```
conda create -p vnenv python==3.13 -y
conda activate vnenv/
```
## Dataset
Student Performance Indicator
https://www.kaggle.com/code/sandeepgauti/student-performance-indicator


# Project Structure
1. `setup.py`: This script is used for packaging and distributing a Python project. This makes your project installable and usable as a Python package.
for local development, run:
    ```
    pip install -e .
    ```
    (This will create .egg-info)

2. `exception.py`: Custom Exception
3. `logger.py`: Custom Logger
4. `utils.py`: Common functions shared across components.



