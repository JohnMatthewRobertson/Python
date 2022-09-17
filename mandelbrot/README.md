# Mandelbrot Development

## Resources

* Make your own mandelbrot (Tariq Rashid)

## Prerequisite

1. Install Docker Desktop:

* https://www.docker.com/products/docker-desktop/

docker desktop version:

```
C:\>docker --version
Docker version 20.10.17, build 100c701
```

2. Install Python 3:

* https://www.python.org/downloads/

```
C:\>python --version
Python 3.9.7
```

3. Install pipenv: 

* https://pypi.org/project/pipenv/

```
C:\>pip show pipenv
Name: pipenv
Version: 2022.9.4
Summary: Python Development Workflow for Humans.
Home-page: https://github.com/pypa/pipenv
Author: Pipenv maintainer team
Author-email: distutils-sig@python.org
License: MIT
Location: d:\python3_9_7\lib\site-packages
Requires: certifi, setuptools, virtualenv, virtualenv-clone
Required-by:
```

4. Down load repository.

## Setup

1. change directory: 

```
cd Python/mandelbrot/mandelbrot_development
``` 

2. start virtual environment 

```
pipenv shell
```

3. install dependencies 

```
pipenv install
```

### linters

1. change directory: 

```
cd Python/mandelbrot
```

2. flake8:

```
flake8 ./mandelbrot_development --exclude=.env > static_code_analysis_output/flake8_output.txt
```

3. pylint:

```
pylint ./mandelbrot_development --ignore=.env > static_code_analysis_output/pylint_output.txt
```

3. bandit:

```
bandit -r ./mandelbrot_development > static_code_analysis_output/bandit_output.txt
```

4. safety:

```
safety check > static_code_analysis_output/safety_output.txt
```

### Tests

1. change directory: 

```
cd Python/mandelbrot/mandelbrot_development
```

2. run coverage 

```
coverage run --source="." manage.py test
```

3. produce coverage report

```
coverage report > ../static_code_analysis_output/coverage_output.txt
```