## Requirements

- Git (of course)
- Python 3 (we use 3.5)
- MySQL
- Node & NPM (we use bower to install dependencies, e.g. the UI components)


## Setup

Cloning the repository:

```sh
git clone https://github.com/BinghamtonCoRE/bikeshare`
```

### Via docker

1) Install Docker Engine. Details [here](https://docs.docker.com/engine/installation/).

2) Build docker image

```sh
docker build -t="bikeshare/app:latest" .
```

### Via virtualenv

1) Create a virtual environment **and activate it**.

2) Install the app's requirements from requirements.txt using pip. **You may need to use pip3 to ensure you're running pip from Python 3.**

```sh
pip install -r requirements.txt
```

4) Install additional required components specified in bower.json using bower.

```sh
bower install
```

5) We have some scripts in the scripts directory for inserting test data to your local database. Assuming you have the local database running, just run the script using Python 3.

6) Configure the app based on the environment you're running it in. If you are developing, you must set the `FLASK_ENVIRONMENT` environment variable to `development`.

```sh
export FLASK_ENVIRONMENT=development
```


## Running the app

### Via docker

There are 2 ways of doing this:

- Via Docker Compose (Installation details [here](https://docs.docker.com/compose/install/)): Recommended Way
    - Set necessary environment variables in `docker-compose.yml` and then run:

    ```sh
    docker-compose up
    ```

- Via Docker Engine

    ```sh
    docker run -p "8000:8000" -it bikeshare/app:latest -e FLASK_ENVIRONMENT='development'
    ```

### Via virtualenv

To start the app simply run the following from the top level directory:

```sh
gunicorn app:app
```

## Contributing

See [CONTRIBUTING.md](https://github.com/BinghamtonCoRE/bikeshare/blob/develop/CONTRIBUTING.md)
