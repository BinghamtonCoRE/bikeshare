## Requirements

- Git (of course)
- Python 3 (we use 3.5)
- Node & NPM (we use bower to install dependencies, e.g. the UI components)

## Setup

1) Fork BinghamtonCoRE/bikeshare. You'll have your own version of the repo at You/bikeshare with both the master branch and develop branch.

2) Create a virtual environment **and activate it**.

3) Install the app's requirements from requirements.txt using pip. **You may need to use pip3 to ensure you're running pip from Python 3.**

```
pip install -r requirements.txt
```

4) Install additional required components specified in bower.json using bower.

```
bower install
```

## Running the app

To start the app simply run the following from the top level directory:

```
gunicorn app:app
```

## Contributing

See [CONTRIBUTING.md](https://github.com/BinghamtonCoRE/bikeshare/blob/develop/CONTRIBUTING.md)