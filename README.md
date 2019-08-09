# Publix Tendies

An installable Python package to determine if Publix brand chicken tender submarine sandwiches are on sale.

## Getting Started

### Development Installation
Follow standard git and Python practices for dev installation.

```bash
$ git clone {repo_url}
$ cd publix-tendies
$ python3 -m venv venv
(publix-tendies)$ pip install -r requirements.txt
```

### Documentation: Sphinx (TODO)
This repo uses [Sphinx] to generate documentation. The Makefile script contains a number of commands which make life easier for the Sphinx user.

To build and serve HTML-compatible documentation, run:
```bash
(publix-tendies)$ make clean
(publix-tendies)$ make html
(publix-tendies)$ python -m http.server
```

From there, documentation will be served at: ``localhost:8000/_build/html``

*Note:* Make sure to `make clean` Sphinx directories before committing code.

## Testing

This repo implements [pytest].  Test configuration is located in `pytest.ini`

[Sphinx]: http://www.sphinx-doc.org
[pytest]: https://docs.pytest.org
