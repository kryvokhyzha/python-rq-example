# python-eq example

This is an example of using the `redis queue` with `FastAPI` backend.

## Setup development environment

1. Clone the repository using `git clone` command.
2. Open the terminal and go to the project directory using `cd` command.
3. Create virtual environment using `python -m venv venv` or
   `conda create -n venv python=3.10` command.
4. Activate virtual environment using `source venv/bin/activate` or
   `conda activate venv` command.
5. Install poetry using instructions from
   [here](https://python-poetry.org/docs/#installation). Use
   `with the official installer` section.
6. Install dependencies using `poetry install --no-root` command. The
   `--no-root` flag is needed to avoid installing the package itself.
7. Setup `pre-commit` hooks using `pre-commit install` command. More information
   about `pre-commit` you can find [here](https://pre-commit.com/).
8. Run the test to check the correctness using following command:
   ```bash
   python -m unittest -b
   ```
