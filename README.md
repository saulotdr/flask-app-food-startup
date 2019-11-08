# Food startup web server 

🐍 [![Python version](https://img.shields.io/badge/python-3.6-blue)](https://python.org)
🌶 [![Flask version](https://img.shields.io/badge/flask-1.1.1-blue)](https://python.org)

## Flow 

This web server implements all the requirements needed by client. The requirements document is available [here](requirements.pdf)

## Configuration

Environment variables to be configured (all are optional):

| Variable | Description | Default value | Accepted values |
| -------- | ----------- | ------------- | --------------- |
| LOGGING_LEVEL | Set the logging level across the module | ERROR | [Logging Levels](https://docs.python.org/3/library/logging.html#levels) |
| PRETTY_PRINT | Modify the response JSON to be indented with 4 spaces and line breaks. | False | Boolean |

## Dependencies

You should install [Pipenv](https://docs.pipenv.org), a package tool for Python that simplifies dependency management.

```bash
$ sudo pip3 install pipenv
```

## Running the flask server

In the project's root folder, run the flask app globally and with the desired port

```
$ export FLASK_APP=src/route.py
$ flask run --host=0.0.0.0 --port=8080
```

## Tests

There are a bunch of types of tests you can run against this Lambda:

- [unit test](tests/unit)




