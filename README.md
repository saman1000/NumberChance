
# UV
I used uv to install a basic API

pip3 install uv
pip3 install --upgrade uv

pip install -e .

uvx fastapi-new chance-api

uv run fastapi dev

# run unit tests
pip install -e ".[test]"

python -m unittest discover -s tests

Or run all unit tests with coverage and then check whether the expected
code coverage fails or passes

coverage run -m unittest discover -s tests

coverage report 